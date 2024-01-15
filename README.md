# FOSDEM'24 Presentation: Daily blogging embedded Gecko development

3/2/2024

FOSS on Mobile devroom
https://fosdem.org/2024/schedule/track/foss-on-mobile-devices/

Daily blogging embedded Gecko development

https://fosdem.org/2024/schedule/event/fosdem-2024-2508-daily-blogging-embedded-gecko-development/

## Details

This folder contains slides for the "Daily blogging embedded Gecko development"
presentation to be given at FOSDEM'24.

## Schedule

Saturday 3rd February 2024, 18:00 -- 18:25 CET

20 minutes talk, 5 minutes question

## Abstract

The Gecko rendering engine is used in many weird and wonderful places. For over a decade it has been the stock rendering engine for the default browser on Sailfish OS, a Linux-based mobile operating system for use on mobile phones and tablets.

The browser implementation was originally developed around the EmbedLite/xulrunner API, which is no longer officially supported. This provides interesting challenges for keeping the browser up-to-date with the latest Gecko changes.

For the last 92 days (maybe more depending on when you're reading this) I've been daily-blogging about my experiences upgrading the ESR 78 Gecko rendering engine used on Sailfish OS to ESR 91. Once ESR 91 is complete the plan is to move to ESR 102 and beyond. Eventually we hope to reach a stable rhythm alongside the official Gecko releases.

This has been a communal effort, with other members of the Sailfish OS community helping with the development, from submitting changes to tooling to creating AI-generated images to liven up the blog posts. Many users from the community are now involved all with the singular aim of getting our Gecko upgraded. The breadth of technologies involved (Rust, C++, JavaScript, Python) makes it a fascinating project to work with and write about.

We've learnt a lot about the Gecko codebase in the process as well as the challenges in deploying Gecko to unusual mobile and embedded platforms. Our hope is that once we reach the latest version, we'll be able to look into contributing more changes upstream to help maintain our Gecko deployment more easily in the future. We'd love to discuss the best way to achieve this.

In this talk I'll share my experiences of working with Gecko in an open way and in collaboration with the community, before opening it out to a discussion about how best to work with upstream.

Links:
1. [Daily dev diary](https://www.flypig.co.uk/gecko)
2. [EmbedLite source](https://github.com/llewelld/gecko-dev)
3. [Sailfish Browser source and issue tracking](https://github.com/sailfishos/sailfish-browser)

## Prebuilt slides

The built slides are available in PDF format from:

https://www.flypig.co.uk/presentations/fosdem24-gecko-dev.pdf

## Building the presentation into a PDF

Requirements:

1. Beamer packages
2. xelatex
3. Source Sans Pro font family:
   https://fonts.google.com/specimen/Source+Sans+Pro

Build the PDF output using the included makefile:
```
make
```

The final output can be found as `fosdem24-gecko-dev.pdf`.

To clean out the intermediary build files and output files:
```
make clean
```

