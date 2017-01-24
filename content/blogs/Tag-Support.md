---
layout: post


date:  "2014-05-30"
aliases: ["/2014/05/30/Tag-Support/"]
title: Tag Support
categories: ["blog"]
comments: true
tags:
   - Jekyll
   - Website
---
The theme now supports tags, tag pages, and a tag cloud.  This functionality requires you to run a utility before pushing your updates to Github Pages.  In order to use tags, you need to add the following information into your YAML front matter:

{% highlight yaml linenos %}
tags:
	- Tag Name (can be multiple words)
{% endhighlight %}

The tag pages will be stored in the /tags directory and the tagcloud.html file (include wherever you want to use it) is saved in the _includes directory.

To create the tag pages and tag cloud, you will need to use the new Rakefile support (see below).  Running `rake deploy` will automatically create the tag pages before committing the changes and pushing to github.

Also, tags support the banner functionality as described.  If either the `banner` id or the `bannertitle` name match the tag name, then that banner will be incorporated on that tag page.

#### Rakefile support:

This website supports the following rake commands:

* `rake post["title"]` - Creates a post with the title "title" and saved into the _posts directory with the current date.  It will then open up your text editor (specified in config.yml).
* `rake draft["title"]` - Similar to post, but this will make it a draft without the post date and will not publish it.
* `rake publish` - Promote a draft posting to a real posting.  It will move the file from the _drafts directory to the _posts directory and will change the post date to the current date.
* `rake page["title"]` - Like posts, but this time with a page.  It is moved to the pages folder by default.
* `rake build` - This will build the tag pages and will also build the full site, but **not** serve it.
* `rake watch` - Builds the site and tags, then serve it.  It will also regenerate on post/page/draft changes.  You can also run `rake watch["drafts"]` which will also preview the draft postings.
* `rake preview` - This will build the site/tags, then open up a web browser to preview the website.
* `rake deploy["Message"]` - This will build the tag pages, add new files to the local git repository, commit the changes with the message "Message", then push the local git repository to your origin master (likely to be github)
* `rake tags` - This will just build the tag pages and tag cloud.

In order to do the post/page publishing, there are two prototype files in the root directory that are named `_post.txt` and `_page.txt` (these names can be updated by changing some variables in the _config.yml file).  

##### 5/27/14
Added an [Archives](/archives/) Page.  It still kinda sucks, but I'll work on it..  Look under the category menu.
