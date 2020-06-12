     __  __  _ __   ____  
    /\ \/\ \/\`'__\/',__\ 
    \ \ \_\ \ \ \//\__, `\
     \ \____/\ \_\\/\____/
      \/___/  \/_/ \/___/ 

This is a universal Reddit scraper that can scrape Subreddits, Redditors, and comments from submissions. 

Written in Python and utilizes the official Reddit API ([ `PRAW` ](https://pypi.org/project/praw/)).

Run `pip install -r requirements.txt` to get all project dependencies. 

You will need your own Reddit account and API credentials for PRAW. I have included a tutorial on how to do this below. 

***NOTE:*** `PRAW` is currently supported on Python 3.5+. This project was tested with Python 3.8.2. 

### Whether you are using this scraper for enterprise or personal use, I am very interested in hearing about your use cases and how it has helped you achieve a goal! If you have enjoyed using this program, found it useful, or have any additional questions, please send me an email at [urs_project@protonmail.com](mailto:urs_project@protonmail.com)!

## Table of Contents

* [URS Overview](#urs-overview)
  + [Table of All Subreddit, Redditor, and Submission Comments Attributes](#a-table-of-all-subreddit-redditor-and-submission-comments-attributes)
  + [Subreddits](#subreddits)
  + [Redditors](#redditors)
  + [Submission Comments](#submission-comments)
* [How to get Reddit API Credentials for PRAW](#how-to-get-reddit-api-credentials-for-PRAW)
* [Walkthrough](#walkthrough)
    - [2-Factor Authentication](#2-factor-authentication)
    - [CLI Scrapers](#cli-scrapers)
      - [Subreddit Scraper](#subreddit-scraper)
      - [Redditor Scraper](#redditor-scraper)
      - [Comments Scraper](#comments-scraper)
    - [Basic Scraper](#basic-scraper)
* [Some Linux Tips](#some-linux-tips)
* [Contributing](#contributing)
* [Contributors](#contributors)
* [Releases](#releases)

# URS Overview

Scrape speeds will be determined by the speed of your internet connection. 

All exported files will be saved within the directory `scrapes/` and stored in a sub-directory labeled with the date. These directories will automatically be created when you run the scraper. 

## A Table of All Subreddit, Redditor, and Submission Comments Attributes

These attributes will be included in each scrape. 

| Subreddits    | Redditors                      | Submission Comments |
|---------------|--------------------------------|---------------------|
| Title         | Name                           | Parent ID           |
| Flair         | Fullname                       | Comment ID          |
| Date Created  | ID                             | Author              |
| Upvotes       | Date Created                   | Date Created        |
| Upvote Ratio  | Comment Karma                  | Upvotes             |
| ID            | Link Karma                     | Text                |
| Is Locked?    | Is Employee?                   | Edited?             |
| NSFW?         | Is Friend?                     | Is Submitter?       |
| Is Spoiler?   | Is Mod?                        | Stickied?           |
| Stickied?     | Is Gold?                       |                     |
| URL           | \*Submissions                  |                     |
| Comment Count | \*Comments                     |                     |
| Text          | \*Hot                          |                     |
| &nbsp;        | \*New                          |                     |
| &nbsp;        | \*Controversial                |                     |
| &nbsp;        | \*Top                          |                     |
| &nbsp;        | \*Upvoted (may be forbidden)   |                     |
| &nbsp;        | \*Downvoted (may be forbidden) |                     |
| &nbsp;        | \*Gilded                       |                     |
| &nbsp;        | \*Gildings (may be forbidden)  |                     |
| &nbsp;        | \*Hidden (may be forbidden)    |                     |
| &nbsp;        | \*Saved (may be forbidden)     |                     |

\*Includes additional attributes; see [Redditors](#redditors) section for more information. 

## Subreddits

`$ ./scraper.py -r SUBREDDIT [H|N|C|T|R|S] N_RESULTS_OR_KEYWORDS --FILE_FORMAT` 

You can specify Subreddits, the submission category, and how many results are returned from each scrape. I have also added a search option where you can search for keyword(s) within a Subreddit and the scraper will get all submissions that are returned from the search. 

These are the submission categories:

* Hot
* New
* Controversial
* Top
* Rising
* Search

***NOTE:*** All results are returned if you search for something within a Subreddit. You will not be able to specify how many results to keep. 

Once you confirm the settings for the scrape, the program will save the results to either a `.csv` or `.json` file. 

The file names will follow this format: `"r-[SUBREDDIT]-[POST_CATEGORY]-[N_RESULTS]-results.[FILE_FORMAT]"` 

If you searched for keywords, file names are formatted as such: `"r-[SUBREDDIT]-Search-'[KEYWORDS]'.[FILE_FORMAT]"` 

## Redditors

`$ ./scraper.py -u USER N_RESULTS --FILE_FORMAT` 

**These scrapes were designed to be used with JSON only. Exporting to CSV is not recommended, but it will still work.**

You can also scrape Redditor profiles and specify how many results are returned. 

Of these Redditor attributes, the following will include additional attributes:

| Submissions, Hot, New, Controversial, Top, Upvoted, Downvoted, Gilded, Gildings, Hidden, and Saved | Comments                                     |
|----------------------------------------------------------------------------------------------------|----------------------------------------------|
| Title                                                                                              | Date Created                                 |
| Date Created                                                                                       | Score                                        |
| Upvotes                                                                                            | Text                                         |
| Upvote Ratio                                                                                       | Parent ID                                    |
| ID                                                                                                 | Link ID                                      |
| NSFW?                                                                                              | Edited?                                      |
| Text                                                                                               | Stickied?                                    |
| &nbsp;                                                                                             | Replying to (title of submission or comment) |
| &nbsp;                                                                                             | In Subreddit (Subreddit name)                |

***NOTE:*** If you are not allowed to access a Redditor's lists, PRAW will raise a 403 HTTP Forbidden exception and the program will just append a "FORBIDDEN" underneath that section in the exported file. 

***NOTE:*** The number of results returned will be applied to all attributes. I have not implemented code to allow users to specify different number of results returned for individual attributes. 

The file names will follow this format: `"u-[USERNAME]-[N_RESULTS]-results.[FILE_FORMAT]"` 

## Submission Comments

`$ ./scraper.py -c URL N_RESULTS --FILE_FORMAT` 

**These scrapes were designed to be used with JSON only. Exporting to CSV is not recommended, but it will still work.**

You can also scrape comments from submissions and specify the number of results returned. 

Comments scraping can either return structured JSON data down to third-level comment replies, or you can simply return a raw list of all comments with no structure. 

To return a raw list of all comments, specify `0` results to be returned from the scrape. 

When exporting raw comments, all top-level comments are listed first, followed by second-level, third-level, etc. 

Of all scrapers included in this program, this takes the longest to scrape. Scraping speed will also depend on the submission's popularity and your internet connection speed.

***NOTE:*** You cannot specify the number of raw comments returned. The program with scrape all comments from the submission. 

The file names will follow this format: `"c-[POST_TITLE]-[N_RESULTS]-results.[FILE_FORMAT]"` 

# How to get Reddit API Credentials for PRAW

1) Create your own Reddit account and then head over to [Reddit's apps page](https://old.reddit.com/prefs/apps). 

2) Click "are you a developer? create an app... ". 

![Create an app](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/Reddit%20API/api_1.png)

3) Name your app, choose "script" for the type of app, and type "http://localhost:8080" in the redirect URI field since this is a personal use app. You can also add a description and an about URL. 

![Enter Stuff In Boxes](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/Reddit%20API/api_2.png)

4) Click "create app", then "edit" to reveal more information. 

![Click Edit](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/Reddit%20API/api_3.png)

5) You should see a string of 14 characters on the top left corner underneath "personal use script. " That is your API ID. Further down you will see "secret" and a string of 27 characters; that is your API password. **Save this information as it will be used in the program in order to use the Reddit API**. 

![All Info](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/Reddit%20API/api_4.png)

You will also have to provide your app name, Reddit account username and password in the block of credentials found on lines 22-26. 

# Walkthrough

First, you will have to provide your own Reddit credentials in this block of code located in `scraper.py`. 

![Reddit credentials](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/creds.png)

URS will raise an error if you entered invalid credentials.

## 2-Factor Authentication

If you choose to use 2FA with your Reddit account, enter your password followed by a colon and then your 2FA token in the `password` field on line 26. For example, if your password is "p4ssw0rd" and your 2FA token is "123456", you will enter "p4ssw0rd:123456" in the `password` field. 

**2FA is NOT recommended for use with this program. ** This is because PRAW will raise an OAuthException after one hour, prompting you to refresh your 2FA token and re-enter your credentials. Additionally, this means your 2FA token would be stored alongside your Reddit username and password, which would defeat the purpose of enabling 2FA in the first place. See [here](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#two-factor-authentication) for more information. 

## CLI scrapers

If you do not want to read the rest of this walkthrough, or forget the args, you can always consult the built-in help message by using `-h` or `--help` . 

![Help Message](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/help.png)

----------------------------------------------------------------------------------------------------------------------------

### Subreddit scraper

Scraping Subreddits using flags is much faster than the [basic scraper](#basic-scraper). 

Use the `-r` flag to indicate a Subreddit, the submission category, and finally, depending on the category selected, either the number of results returned or keyword(s) to search for during the scrape. 

Category options are as follows:

 - H, h - Hot
 - N, n - New
 - C, c - Controversial
 - T, t - Top
 - R, r - Rising  
 - S, s - Search
 
Scraping 10 r/AskReddit posts in the Hot category and export to JSON:

![Subreddit Scraping 1](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/r_1.png)

The program will then display the type of scrape, check if the Subreddit(s) exist, and display the settings for each Subreddit. It will display a list of invalid Subreddits if applicable. You can also include `-y` in your args if you want to skip this confirmation screen and immediately scrape. 

![Subreddit Scraping 2](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/r_2.png)

**JSON Sample:**

![JSON Sample](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/r_json.png)

**CSV Sample:**

![CSV Sample](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/r_csv.png)

---------------------------------------------------------------------------------------------------------------------------- 

### Redditor Scraper

Use the `-u` flag to indicate a Redditor and the number of results returned. The program will then display the type of scrape and check if the Redditor(s) exist. It will display a list of invalid Redditors, if applicable. 

**These scrapes were designed to be used with JSON only. Exporting to CSV is not recommended, but it will still work.** 

Scraping 5 results for each of u/spez's user attributes and export to JSON:

![Redditor Scraping 1](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/u_1.png)

There are a couple user lists that are typically restricted and will raise an 403 HTTP Forbidden exception. If you are forbidden from accessing a list, the program will display its name and append "FORBIDDEN" to that section in the export file. 

![Redditor Scraping 2](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/u_2.png)

**JSON Sample:**

![Redditor JSON](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/u_json.png)

----------------------------------------------------------------------------------------------------------------------------

### Comments Scraper

Use the `-c` flag to indicate a submission and the number of comments returned. The program will then display the type of scrape and check if the submission(s) exist. It will display a list of invalid posts, if applicable. 

**These scrapes were designed to be used with JSON only. Exporting to CSV is not recommended, but it will still work.** 

There are two ways you can scrape comments with this program. You can indicate a number to return a structured JSON file that includes down to third-level replies. Or you can specify `0` comments to be returned and the program will return an unstructured JSON file of all comments. 

**Structured Scrape**

Scraping 10 comments from [this Reddit submission](https://www.reddit.com/r/ProgrammerHumor/comments/9ozauu/a_more_accurate_representation_of_what_happened/) and export to JSON:
 

![Comments Scraping 1](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/c_1.png)

![Comments Scraping 2](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/c_2.png)

**Structured JSON Sample:**

![Structured JSON](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/c_json.png)

**Unstructured Scrape**

When exporting raw comments, all top-level comments are listed first, followed by second-level, third-level, etc. 

![Comments Scraping 3](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/c_3.png)

![Comments Scraping 4](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/c_4.png)

**Unstructured JSON Sample:**

![Unstructured JSON](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/c_json_raw.png)

## Basic Scraper

I kept URS 1.0's functionality after I added CLI support, in case anyone prefers to use it over CLI arguments. **It only scrapes Subreddits**; Redditor and submission comments scraping would require you to use CLI arguments. 

You can access the basic scraper by using the `-b` flag and an export option. 

You can just scrape a single Subreddit, or enter a list of Subreddits separated by a space. 

![B Flag](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/b_1.png)

After entering the Subreddit(s) you want to scrape, the program will check if the Subreddit exists. It will separate the results into a list of valid and invalid Subreddits. 

![Check Subs](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/b_2.png)

You will then choose the submission category within the Subreddit (Hot, New, Controversial, Top, Rising, or Search). After choosing the category, you will also choose how many results you would like to be returned. 

![Submission Category Options](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/b_3.png)

If you choose to search for keyword(s) within the Subreddit, you will be greeted with these settings instead. 

![Search](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/b_4.png)

After you have configured all settings for each Subreddit, you will be greeted with the following screen which displays all of your settings. After confirming, the program will scrape the Subreddits based on your parameters. 

![Settings Overview](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/b_5.png)

![Settings Overview](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/Screenshots/b_6.png)

# Some Linux Tips

* You can further simplify running the program by making the program executable. 
* `sudo chmod +x scraper.py` 
* Make sure the shebang at the top of scraper. py matches the location in which your Python is installed. You can use `which python` to check. The default shebang is `#!/usr/bin/python` . 
* Now you will only have to prepend `./` to run the scraper. 
  + `./scraper.py ...` 
* Troubleshooting
  + If you run the scraper with `./` and are greeted with a bad interpreter error, you will have to set the fileformat to UNIX. I did this using Vim. 

	``` 
    vim scraper.py
    :set fileformat=unix
    :wq!
    ```

# Contributing

I believe the current features should satisfy users who need to scrape Reddit; however, I will continue adding small features as I learn more about computer science.

You can suggest new features or changes by going to the Issues tab, creating a new issue, and tagging it as an enhancement. If there are good suggestions and a good reason for adding a feature, I will consider adding it. 

You are also more than welcome to create a pull request, adding additional features, improving runtime, or streamlining existing code. If the pull request is approved, I will merge the pull request into the master branch and credit you for contributing to this project.

Make sure you follow the contributing guidelines when creating a pull request. See the [Contributing](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/CONTRIBUTING.md) document for more information. 

# Contributors

| Date           | User                                                      | Contribution                                                                                                               |
|----------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| March 11, 2020 | [ThereGoesMySanity](https://github.com/ThereGoesMySanity) | Created a [pull request](https://github.com/JosephLai241/Universal-Reddit-Scraper/pull/9) adding 2FA information to Readme |

# Releases

| Release Date | Version | Changelog | 
|--------------|---------|-----------|
| **May 25, 2019** | URS v1.0 | <ul> <li>Its inception.</li> </ul> |
| **July 29, 2019** | URS v2.0 | <ul> <li>Now includes CLI support!</li> </ul> |
| **December 28, 2019** | URS v3.0 (beta) | <ul> <li>Added JSON export.</li> <li>Added Redditor Scraping.</li> <li>Comments scraping is still under construction.</li> </ul> | 
| **December 31, 2019** | URS v3.0 (Official) | <ul> <li>Comments scraping functionality is now working!</li> <li>Added additional exception handling for creating filenames.</li> <li>Minor code reformatting.</li> <li>Simplified verbose output.</li> <li>Added an additional submission attribute when scraping Redditors.</li> <li>Happy New Year!</li> </ul> |
| **January 15, 2020** | URS v3.0 (Final Release) | <ul> <li>Numerous changes to Readme.</li> <li>Minor code reformatting.</li> <li>Fulfilled community standards by adding the following docs:</li> <ul> <li>[Contributing Guidelines](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/CONTRIBUTING.md)</li> <li>[Pull Request Template](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/PULL_REQUEST_TEMPLATE.md)</li> <li>Issue templates:</li> <ul> <li>[Bug Report](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/ISSUE_TEMPLATE/BUG_REPORT.md)</li> <li>[Feature Request](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/ISSUE_TEMPLATE/FEATURE_REQUEST.md)</li> </ul> <li>[Code of Conduct](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/.github/CODE_OF_CONDUCT.md)</li> <li>[License](https://github.com/JosephLai241/Universal-Reddit-Scraper/blob/master/LICENSE)</li> </ul> </ul> |
| **TBD** | URS v3.1 | <ul> <li>***Major*** code refactor. Applied OOP concepts to existing code and rewrote methods in attempt to improve readability, maintenance, and scalability.</li> <li>Scrapes will now be exported to the `scrapes/` directory within a subdirectory corresponding to the date of the scrape. These directories are automatically created for you when you run URS.</li> <li>Added log decorators that record what is happening during each scrape, which scrapes were ran, and any errors that might arise during runtime in the log file `scrapes.log`. The log will be stored in the same subdirectory corresponding to the date of the scrape.</li> <li>Added color to terminal output.</li> <li>Improved naming convention for scripts.</li> <li>***UPDATE COMMUNITY DOCS WHEN DONE REFACTORING.***</li> <li>Numerous changes to Readme.</li> </ul> | 
