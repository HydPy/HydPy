# HydPy Website
Website of HydPy - _Hyderabad Python User Group_

## Dev Setup
The site uses [jekyll](https://jekyllrb.com/) a simple and popular static website generator which can be hosted via [github pages](https://pages.github.com/). You can quickly start developing by pushing your code to the `gh-pages` branch of your repo. Then go to the `Settings` tab of your GitHub account, scroll down to the `GitHub Pages` section and choose `gh-pages` as source. But this will need you to push the code to gh-pages everytime you wish to test out a change.

We **recommend** doing development in offline. For that you need ruby to be installed in your local since jekyll is a ruby gem. Follow these steps for installation in local.

1. Install Ruby as per this [installation guide](https://www.ruby-lang.org/en/documentation/installation/). For Linux, Mac OSX it's preferable to use [RVM](https://rvm.io/) and for Windows you can use [RubyInstaller](https://rubyinstaller.org/)
2. Run `gem install bundler jekyll`. This install bundler and jekyll.
3. Run `bundle install`
4. Run `bundle exec jekyll serve` to start the server
5. Site is up and running! Go to `localhost:4000`

## Adding Content

### Event post
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

### FAQ Question entry
Create a Question entry (that is listed in the Frequently Asked section on the Home page) in this directory by creating a file called `yyyy-mm-dd-do-i-have-a-question.markdown` in the `/_faqs/` directory with the following template:
```markdown
---
layout: question
title:  "Do I have a question?"
---

Can I use this theme for my website?
Of course you can!
```

