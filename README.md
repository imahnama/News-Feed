# News-Feed
A primitive news feed is very simple application that allows users to post information to a feed and also view information on the feed. Additionally, users can view comments on particular posts as well as commenting on posts

## Commands

    Usage:
        primfeed view_feed
        primfeed post <title> <body>
        primfeed comment <postId> <title> <body>
        primfeed (-i | --interactive)
        primfeed (-h | --help | --version)
    Options:
        view_feed Returns a list of all posts
        post  adds a new post
        <title>  represents the title of the new resource
        <body>  represents the body of the new resource
        comment  adds a new comment to a post, see postid
        <postId>  specifies the post id
        -i, --interactive  Interactive Mode
        -h, --help  Show this screen and exit.
        
### Functions

primfeed view_feed : Returns all posts as list
    
primfeed post <title> <body>
    e.g. primefeed post New "New Post" "This is the body"
    
primfeed comment <postID> <title> <body>
    e.g. primefeed comment 2 "New Comment" "This is the body of the comment"
    
    
