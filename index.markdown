---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: splash
header:
  image: images/banners/grand_canyon.jpeg
intro:
  - excerpt: 'Welcome to my website!  Check out my [**About**](/about) page to learn about who I am.  See my [**Projects**](/projects) or [**Adventures**](/adventures) pages to read about my exploits.'
feature_row:
  - image_path: images/thumbnails/enchilada.jpeg
    title: "About"
    #excerpt: "I'm a physicist/mathematician/engineer with a passion for mountain biking, skiing, and exploring the outdoors."
    url: /about/
    #btn_label: "Read More"
    #btn_class: "btn--primary"
  - image_path: images/thumbnails/rollins.jpeg
    title: "Projects"
    #excerpt: "I tinker with electronics, software, and just about everything else."
    url: /projects/
    #btn_label: "Read More"
    #btn_class: "btn--primary"
  - image_path: images/thumbnails/sedona.jpg
    title: "Adventures"
    #excerpt: "I take my bikes, skis, or climbing gear with me whenever I feel the call of the wild."
    url: /adventures/
    #btn_label: "Read More"
    #btn_class: "btn--primary"
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}
