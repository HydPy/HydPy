# HydPy
HydPy - Hyderabad Python User Group Website

##Dev Setup
TODO

##Usage
This theme can be customized, built and published straight from GitHub, thanks to [GitHub Pages](https://pages.github.com/). A local installation of Jekyll isn't even necessary!

####Customize  
#####Event post
Create a Event post by creating a file called `yyyy-mm-dd-name-of-post-like-this.markdown` in the `/_posts/` directory with the following template:
```markdown
---
layout: post          #important: don't change this
title: "Name of post like this"
venue: "Location of event"
location: "google maps url link"
location-embedded: "google maps embedded url link"
date: yyyy-mm-dd hh:mm:ss
presenter: Name
meetup: "meetup link"
categories:
- python                #important: leave this here
- category1
- category2
- ...
img: post01.jpg       #place image (850x450) with this name in /assets/img/blog/
thumb: thumb01.jpg    #place thumbnail (70x70) with this name in /assets/img/blog/thumbs/
---
This text will appear in the excerpt "Event preview" on the Events page that lists all the posts.
<!--more-->
This text will not be shown in the excerpt because it is after the excerpt separator.
```
#####FAQ Question entry
Create a Question entry (that is listed in the Frequently Asked section on the Home page) in this directory by creating a file called `yyyy-mm-dd-do-i-have-a-question.markdown` in the `/_faq/` directory with the following template:
```markdown
---
layout: question
title:  "Do I have a question?"
---
####Can I use this theme for my website?
Of course you can!
```

