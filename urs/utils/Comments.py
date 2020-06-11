#===============================================================================
#                               Comments Scraping
#===============================================================================
from colorama import Fore, init, Style

from . import Cli, Export, Global, Titles, Validation
from .Logger import LogExport, LogScraper

### Automate sending reset sequences to turn off color changes at the end of 
### every print.
init(autoreset = True)

### Global variables.
convert_time = Global.convert_time
eo = Global.eo
s_t = Global.s_t

class PrintPosts():
    """
    Function for printing found and invalid Reddit posts.
    """

    ### Check if posts exist and list posts that are not found.
    @staticmethod
    def list_posts(reddit, post_list, parser):
        print("\nChecking if post(s) exist...")
        posts, not_posts = Validation.Validation.existence(s_t[2], post_list, 
            parser, reddit, s_t)
        if not_posts:
            print(Fore.YELLOW + Style.BRIGHT + 
                "\nThe following posts were not found and will be skipped:")
            print(Fore.YELLOW + Style.BRIGHT + "-" * 55)
            print(*not_posts, sep = "\n")

        if not posts:
            print(Fore.RED + Style.BRIGHT + "\nNo submissions to scrape!")
            print(Fore.RED + Style.BRIGHT + "\nExiting.\n")
            quit()

        return posts

class GetComments():
    """
    Functions for getting comments from a post.
    """

    ### Initialize objects that will be used in class methods.
    def __init__(self):
        self._titles = ["Parent ID", "Comment ID", "Author", "Date Created", "Upvotes", 
            "Text", "Edited?", "Is Submitter?", "Stickied?"]

    ### Handle deleted Redditors or edited time if applicable.
    def _fix_attributes(self, comment):
        try:
            author_name = comment.author.name
        except AttributeError:
            author_name = "[deleted]"

        edit_date = comment.edited if str(comment.edited).isalpha() \
            else convert_time(comment.edited)

        return author_name, edit_date

    ### Add list of dictionary of comments attributes to use when sorting.
    def add_comment(self, comment):
        c_set = Global.make_none_dict(self._titles)

        author_name, edit_date = self._fix_attributes(comment)
        comment_attributes = [comment.parent_id, comment.id, author_name, 
            convert_time(comment.created_utc), comment.score, comment.body, edit_date, 
            comment.is_submitter, comment.stickied]

        for title, attribute in zip(self._titles, comment_attributes):
            c_set[title] = attribute
        
        return [c_set]

class SortComments():
    """
    Functions for sorting comments depending on which style of comments was 
    specified (raw or structured).
    """

    ### Append comments in raw export format.
    @staticmethod
    def _raw_comments(all_dict, comment):
        add = GetComments().add_comment(comment)
        all_dict[comment.id] = add

    ### Append top level comments to all_dict.
    @staticmethod
    def _top_level_comment(all_dict, comment):
        add = GetComments().add_comment(comment)
        all_dict[comment.id] = [add]

    ### Append second-level comments to all_dict.
    @staticmethod
    def _second_level_comment(all_dict, comment, cpid):
        append = GetComments().add_comment(comment)
        all_dict[cpid].append({comment.id:append})

    ### Append third-level comments to all_dict.
    @staticmethod
    def _third_level_comment(all_dict, comment, cpid):
        for more_comments in all_dict.values():
            for item in more_comments:
                if isinstance(item, dict):
                    sub_set = GetComments().add_comment(comment)
                    if cpid not in item.keys():
                        item[comment.id] = [sub_set]
                    else:
                        item[cpid].append({comment.id:sub_set})

    ### Appending structured comments to all_dict.
    @staticmethod
    def _structured_comments(all_dict, comment, cpid, submission):
        if cpid == submission.id:
            SortComments._top_level_comment(all_dict, comment)
        elif cpid in all_dict.keys():
            SortComments._second_level_comment(all_dict, comment, cpid)
        else:
            SortComments._third_level_comment(all_dict, comment, cpid)

    ### Append comments to all dictionary differently if raw is True or False.
    @staticmethod
    def _to_all(all_dict, comment, raw, submission):
        if raw:
            SortComments._raw_comments(all_dict, comment)
        else:
            cpid = comment.parent_id.split("_", 1)[1]
            SortComments._structured_comments(all_dict, comment, cpid, submission)

    ### Sort comments.
    @staticmethod
    def sort(all_dict, raw, submission):
        for comment in submission.comments.list():
            SortComments._to_all(all_dict, comment, raw, submission)

class GetSort():
    """
    Functions for getting comments from a Reddit submission.
    """

    ### Initialize objects that will be used in class methods.
    def __init__(self, post, reddit):
        self._submission = reddit.submission(url = post)

        print(Fore.YELLOW + Style.BRIGHT + "\nResolving instances of MoreComments...")
        print("\nThis may take a while. Please wait.")
        self._submission.comments.replace_more(limit = None)

    ### Get comments in raw format.
    def _get_raw(self, all_dict, submission):
        print(Style.BRIGHT + 
            "\nProcessing all comments in raw format from Reddit post '%s'..." % 
                submission.title)

        SortComments().sort(all_dict, True, submission)

    ### Get comments in structured format.
    def _get_structured(self, all_dict, limit, submission):
        plurality = "comment" if limit == 1 else "comments"
        print(Style.BRIGHT + 
            ("\nProcessing %s %s including second and third-level replies from Reddit post '%s'...") % 
                (limit, plurality, submission.title))

        SortComments().sort(all_dict, False, submission)
        all_dict = {key: all_dict[key] for key in list(all_dict)[:int(limit)]}

    ### Get comments from posts.
    def get_sort(self, limit, post, reddit):
        all_dict = dict()

        self._get_raw(all_dict, self._submission) if int(limit) == 0 else \
            self._get_structured(all_dict, limit, self._submission)

        return all_dict

class Write():
    """
    Functions for writing scraped comments to CSV or JSON.
    """

    ### Export to either CSV or JSON.
    @staticmethod
    def _determine_export(args, f_name, overview):
        Export.Export.export(f_name, eo[1], overview) if args.json else \
            Export.Export.export(f_name, eo[0], overview)

    ### Print confirmation message and set print length depending on string length.
    @staticmethod
    def _print_confirm(args, title):
        confirmation = "\nJSON file for '%s' comments created." % title \
            if args.json else \
                "\nCSV file for '%s' comments created." % title
        
        print(Style.BRIGHT + Fore.GREEN + confirmation)
        print(Style.BRIGHT + Fore.GREEN + "-" * (len(confirmation) - 1))

    ### Get, sort, then write scraped comments to CSV or JSON.
    @staticmethod
    def write(args, c_master, post_list, reddit):
        for post, limit in c_master.items():
            title = reddit.submission(url = post).title
            overview = GetSort(post, reddit).get_sort(limit, post, reddit)
            f_name = Export.NameFile().c_fname(limit, title)

            Write._determine_export(args, f_name, overview)
            Write._print_confirm(args, title)

class RunComments():
    """
    Run the comments scraper.
    """

    ### Run comments scraper.
    @staticmethod
    @LogExport.log_export
    @LogScraper.scraper_timer(Global.s_t[2])
    def run(args, parser, reddit):
        Titles.Titles().c_title()

        post_list = Cli.GetScrapeSettings().create_list(args, s_t[2])
        posts = PrintPosts.list_posts(reddit, post_list, parser)
        c_master = Global.make_none_dict(posts)
        Cli.GetScrapeSettings().get_settings(args, c_master, reddit, s_t[2])

        Write.write(args, c_master, post_list, reddit)
