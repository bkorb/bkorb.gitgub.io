---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: splash
header:
  image: /assets/images/header2.jpeg
intro: 
  - excerpt: 'Welcome to my website!'
feature_row:
  - image_path: assets/images/zion.jpg
    title: "Placeholder 1"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
  - image_path: /assets/images/rollins.jpeg
    title: "Placeholder 2"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
    url: /jekyll/update/2021/12/27/welcome-to-jekyll.html
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: /assets/images/sedona.jpg
    title: "Placeholder 3"
    excerpt: "This is some sample content that goes here with **Markdown** formatting."
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}
