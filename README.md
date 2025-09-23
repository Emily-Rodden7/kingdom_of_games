# Kingdom Of Games

Link to deployed site: [kingdomofgames](https://kingdom-of-games-f3145b6a77c9.herokuapp.com/)

[Go to TESTING.md file to see screenshots](TESTING.md)

Welcome to Kingdom Of Games, an e-commerce website offering a vast collection of board games for every kind of player, from children’s classics and family-friendly fun to adults-only party games, including drinking and NSFW options.

This site was built to create a vibrant, easy-to-navigate digital storefront where users can discover, browse, and purchase the best board games in one place. Whether you're shopping for a quiet game night with the kids, a competitive family evening, or a wild party game for adults; Kingdom Of Games has you covered.

## UX (User Experience)

### Design & Colour Scheme

The site was designed to evoke fun, nostalgia, and curiosity. The layout is clear and easy to navigate, catering to users of all ages, from casual shoppers to seasoned game collectors.

Main Color: Royal Blue – symbolizing trust, fun, and tradition.

Accent Color: Gold – representing premium quality and excitement.

## User Stories

1. Browse Games by Category: As a user,
- I want to browse games by category (family, kids, 18+),
- So I can quickly find the type of game I’m interested in.

2. Search for Specific Games: As a user,
- I want to search for games by title or keyword,
- So I can find exactly what I’m looking for without browsing.

3. As a casual browser,
- I want to filter games by category (e.g. strategy, children, card games),
- so that I can find the kind of games I enjoy.

4. User Account Management: As a user,
- I want to register and log in to my account,
- So I can view order history, save favorites, and manage my personal info.

5. Purchase Games Easily: As a user,
- I want to add games to a cart and checkout securely,
- So I can buy games conveniently from home.

6. Leave and Read Game Reviews: As a user,
- I want to read and write reviews,
- So I can learn from others and share my experiences.

## Wireframes

Home Page

Game Category Page

Individual Game Page

Login & Sign Up

User Dashboard

Cart & Checkout

Admin Backend

## Features

### Site Pages

Screenshots of the finished pages.

Home: Showcases top categories and featured games.

Browse Games: View all games or filter by type (e.g., Kids, Family, 18+).

Game Detail Page: Shows all relevant info, pricing, age restrictions, and reviews.

Sign Up / Login: Secure user authentication.

User Dashboard: View orders, manage wishlist, update profile.

Shopping Cart & Checkout: Integrated e-commerce flow.

Admin Panel: Allows site owner to manage products, users, and orders.

### User Features

- Account creation and login

- Add/remove from wishlist

- Checkout with address form and order summary

- Order history tracking

- Edit account details

- Button to take user back to the top of the page

## Future Features

- Game rental service (limited-time play)

- Community forums or chat

- Game night event scheduling

- Loyalty points system

- Gift cards and wishlists for birthdays/holidays

## Tools & Technologies Used

- HTML/CSS/JavaScript — Core front-end development

- Bootstrap — UI layout and responsiveness

- Python/Django — Backend framework

- PostgreSQL — Database

- Stripe — Payment processing

- Heroku — Deployment

- Git/GitHub — Version control

- Code Institute tutorial videos and documents

## Testing

[Go to TESTING.md file to see screenshots](TESTING.md)

Testing included:

- Manual testing of forms, filtering, cart logic, and user accounts

- Mobile responsiveness on iOS and Android

- Compatibility with Chrome, Safari, Firefox

- Form validation and field error handling

- Admin permissions and product editing

## Deployment

Deployed on [Heroku](https://www.heroku.com/) using the following:

- requirements.txt generated with pip freeze

- Procfile created to run gunicorn

- Config vars added in Heroku dashboard

- Connected GitHub repo for automatic deployment

- The live deployed application can be found deployed on [Heroku.](https://kingdom-of-games-f3145b6a77c9.herokuapp.com/)

### The Process

- This project uses Heroku, a Platform-as-a-Service (PaaS) that allows developers to build, run, and manage applications entirely in the cloud. Follow these steps to deploy your app after setting up your account:

- In the top-right corner of your Heroku Dashboard, click on New, then select Create new app from the dropdown menu.

- Choose a unique name for your app, select a region (either EU or USA), and click Create App.

- Once your app is created, go to the Settings tab, click on Reveal Config Vars, and set your environment variables.

- Heroku requires two files to deploy your app correctly: requirements.txt Procfile To install the necessary dependencies, run: pip3 install -r requirements.txt

- If you have additional packages installed, update the requirements.txt file with: pip3 freeze --local > requirements.txt

- To create the Procfile, use the following command: echo web: gunicorn app_name.wsgi > Procfile

- Replace app_name with the name of your main Django app (the folder containing settings.py).

- Connecting Your GitHub Repository and Deploying: Option 1:

- Go to the Deploy tab of your Heroku app and select Automatic Deployment.

- Option 2:

- In your terminal, log in to Heroku with the following command: heroku login -i

- Set the Heroku remote repository: heroku git:remote -a app_name (Make sure to replace app_name with the actual name of your app.)

- Perform the standard Git commands (git add, git commit, and git push), and finally, push your changes to Heroku with: git push heroku main

- Your project should now be connected and deployed on Heroku!

## Admin Backend

Using [Django’s admin panel](https://kingdom-of-games-f3145b6a77c9.herokuapp.com/admin/login/?next=/admin/), the superuser can:

- Add/edit/delete products

- Process or cancel orders

- Manage subscribers, add, edit or delete

## Media & Assets

### Images used

- [home page hero](https://www.underdoggames.com/a/blog/family-game-night?srsltid=AfmBOoqCf1u6UfvYDBo27be2EHtWn02VyC6DG4bbeoxUXGKgvF0BsdDF)


- [p for pizza](https://bigpotato.co.uk/products/p-for-pizza)

- [dobble](https://www.garage-bar.co.uk/product/dobble-original-card-game/)

- [catan](https://www.argos.co.uk/product/9498259)

- [hues and cues](https://www.amazon.co.uk/USAopoly-USOPA135725-Hues-and-Cues/dp/B084D2XQ9F/ref=asc_df_B084D2XQ9F?mcid=ebf1516c260a3dcab8f9729d165455ca&tag=googshopuk-21&linkCode=df0&hvadid=696350735931&hvpos=&hvnetw=g&hvrand=13554249309985677979&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-932403467182&psc=1&hvocijid=13554249309985677979-B084D2XQ9F-&hvexpln=0&gad_source=1)

- [yatzee](https://www.amazon.co.uk/Yahtzee-Classic-Family-Dice-Game/dp/B00TLEMRKM/ref=asc_df_B00TLEMRKM?mcid=18c7c7bf72cc3f5cb4ddc9574315c46a&tag=googshopuk-21&linkCode=df0&hvadid=696350735931&hvpos=&hvnetw=g&hvrand=3241969677952768441&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-437430439153&psc=1&hvocijid=3241969677952768441-B00TLEMRKM-&hvexpln=0&gad_source=1)

- [Info for strategy games](https://www.nytimes.com/wirecutter/reviews/best-strategy-board-games/)

- [Carcassonne](https://www.amazon.co.uk/Gl%C3%BCck-Carcassonne-Family-Players-Minutes/dp/B0B1F2872Z/ref=asc_df_B0B1F2872Z?mcid=d7149a0dd5073a8ab91c3074e240e26c&tag=googshopuk-21&linkCode=df0&hvadid=696350735931&hvpos=&hvnetw=g&hvrand=13790789557735701855&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-1876398777059&hvocijid=13790789557735701855-B0B1F2872Z-&hvexpln=0&gad_source=1&th=1)

- [mouse trap](https://www.amazon.co.uk/Classic-Players-Easier-Previous-Versions/dp/B09PV9LYXS/ref=asc_df_B09PV9LYXS?mcid=2ea99e02077c32ad9014afc946bc8cd7&tag=googshopuk-21&linkCode=df0&hvadid=697344814787&hvpos=&hvnetw=g&hvrand=3743813038291630707&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-1696447665087&psc=1&hvocijid=3743813038291630707-B09PV9LYXS-&hvexpln=0&gad_source=1)

- [kerplunk](https://www.amazon.co.uk/Spiel/dp/B0DNJH5RRW)

- [sorry](https://www.amazon.co.uk/Hasbro-Gaming-A5065-Sorry-Game/dp/B076HK9H7Z/ref=asc_df_B076HK9H7Z?mcid=3d434518f58937d399d8d91590449579&tag=googshopuk-21&linkCode=df0&hvadid=697281466526&hvpos=&hvnetw=g&hvrand=3743813038291630707&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-491700295819&hvocijid=3743813038291630707-B076HK9H7Z-&hvexpln=0&gad_source=1&th=1)

- [hungry hippos](https://www.amazon.co.uk/Hungry-Hippos-Board-Game/dp/B0CQ59PGGF/ref=asc_df_B0CQ59PGGF?mcid=120396ea2dd735298eb10364af7533f5&th=1&tag=googshopuk-21&linkCode=df0&hvadid=697344814787&hvpos=&hvnetw=g&hvrand=15721922052769072771&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-2394378966629&hvocijid=15721922052769072771-B0CQ59PGGF-&hvexpln=0&gad_source=1)

- [monopoly](https://www.amazon.co.uk/Monopoly-Family-Board-Players-Community/dp/B096W2XGHM/ref=asc_df_B096W2XGHM?mcid=a02d11b0f8da36e0b07d249ea23cec80&th=1&tag=googshopuk-21&linkCode=df0&hvadid=697281466526&hvpos=&hvnetw=g&hvrand=16024363162974855860&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-1519919335827&hvocijid=16024363162974855860-B096W2XGHM-&hvexpln=0&gad_source=1)

- [cluedo](https://www.amazon.co.uk/Hasbro-Gaming-Reimagined-Players-Detective/dp/B0BSLFD2RC/ref=sr_1_1?crid=JHEGCZBZJP2Q&dib=eyJ2IjoiMSJ9.n0t9QCfbaBug1rn8a2Ynu2mZ4q8txltjTwOgP2JHRm5V_wXWsn8G96jLxUA_B-W3PbyJDlVXHZvvGeyi2QzBFjJFikt0G1RADQtSDU65o9EACVZJ6rFd-828SeJptP9wopPps6E5ouYW4_eCUMplqKnFrxqCd-nVhyzi2zbqj57GV_vIrzMuzPl--gj8RbVqvIPTtag80qbFirCiP-5-Dn2OZD_0EPreY0lkOW4RTt-INQFtYLSzekFQ8I8RYK51TW_l7G1p_dtLWzI9uqMyPs2CG73HT7EB4UioAhKlw74.QeLKx97RPx8ghKGugSSj_A6vb-7XJmCpvjVG3m4U_IY&dib_tag=se&keywords=cluedo&qid=1758048156&s=kids&sprefix=cluedo%2Ctoys%2C168&sr=1-1&th=1)

- [chess](https://www.amazon.co.uk/Classic-Chess-Children-Traditional-Instructions/dp/B0D47N6S43/ref=sr_1_4?crid=33APSSVHKI6C7&dib=eyJ2IjoiMSJ9.iGJMgB4lxKef4fEmCPrVlymIkx7g5Hz1SNhjtQwhGpLdDgjbrkz2nFq7BRJy0RoQNE0aP7eTy5w19YsG4CynuSL36Ab-70LZtEuvHEssKDK3WcE0p5jXjvxBj90BU1lWBfRIMl2_NjzDeq2cMjVkSBGWgeAH3vRxN_TnC6Ynw2HRxlCJ6Ov0uYpXCtPZ2cvmkgTgvf5mMZEV_jaojhXM5qHrkElAHO6HyxPkcJn6Ohx9m9WBSHnXNpcXc5F2X_iiFwIuTQPpHbkTU1jKMx64jJiOxMac_O4tIGqBvDCVrP8.iiyYOaWm9kwqZOEY3dVJoM6YkTKJBdqze5_ARiuSTPU&dib_tag=se&keywords=chess&qid=1758048184&s=kids&sprefix=ches%2Ctoys%2C209&sr=1-4&th=1)

- [image coming soon](https://castlewoodassistedliving.com/image-coming-soon-placeholder/)

- [cards against humanity](https://www.amazon.co.uk/Cards-Against-Humanity-UK-Edition/dp/B09X9CRNLD)

- [do or drink](https://www.therange.co.uk/toys/puzzles-board-and-card-games/card-games/do-or-drink-win-or-blackout-edition?utm_source=google&utm_medium=cpc&utm_campaign=22765680476-&utm_content=-&utm_term=&gad_source=1&gad_campaignid=22759609827&gbraid=0AAAAADFuktyrj955sRXQmwn-JlZEvIShJ&gclid=Cj0KCQjwuKnGBhD5ARIsAD19RsbX2ioEqq9ISX3Tjg_lxOO8yXFLQhwVOG_WpdGHYcrJObmcZ963tcYaAplREALw_wcB#380874)

- [monopoly drinking game](https://www.amazon.co.uk/Monopoly-G1298-Board-Crawl/dp/B0D2JK8QFL/ref=asc_df_B0D2JK8QFL?mcid=5bb69fd0645d3d07858f6558e4087477&th=1&psc=1&tag=googshopuk-21&linkCode=df0&hvadid=712027622340&hvpos=&hvnetw=g&hvrand=18407623419091235866&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-2370303190760&psc=1&hvocijid=18407623419091235866-B0D2JK8QFL-&hvexpln=0&gad_source=1)

- [tispy land](https://www.menkind.co.uk/tipsy-land-board-game?gad_source=1&gad_campaignid=23031961126&gbraid=0AAAAAD45wmHsY-9JvpBtMlNtfPke-YcyM&gclid=Cj0KCQjwuKnGBhD5ARIsAD19Rsbdg3Wbe_IuKoE7ID5f-EulyZL81F5TghKRwiICx2pz6cdE5XFSdtoaAhvNEALw_wcB)

- [Horrible Therapist](https://www.explodingkittens.com/products/horrible-therapist-worst-edition)

- [exploding kitten nsfw](https://www.explodingkittens.com/products/exploding-kittens-nsfw-edition)

- [poetry nsfw](https://www.explodingkittens.com/products/poetry-for-neanderthals-nsfw-edition)

- [ticket to ride](https://www.amazon.co.uk/Days-Wonder-7201-Ticket-Ride/dp/0975277324)

- [Taco](https://www.amazon.co.uk/Blue-Orange-BLUTACO-Cheese-Colours/dp/B088HRRB59/ref=asc_df_B088HRRB59?mcid=0d74f0eaa23c355bb0c00de73d557d02&th=1&tag=googshopuk-21&linkCode=df0&hvadid=696350735931&hvpos=&hvnetw=g&hvrand=3127525745372442187&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-917513888559&hvocijid=3127525745372442187-B088HRRB59-&hvexpln=0&gad_source=1)

- [UNO](amazon.co.uk/UNO-W2087-Card-Game-European/dp/B005I5M2F8/ref=asc_df_B005I5M2F8?mcid=af7deb2899a632fcb69d0615767503c0&tag=googshopuk-21&linkCode=df0&hvadid=696350735931&hvpos=&hvnetw=g&hvrand=3127525745372442187&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-385946056070&psc=1&hvocijid=3127525745372442187-B005I5M2F8-&hvexpln=0&gad_source=1)

- [hedbanz](https://www.amazon.co.uk/Spin-Master-Games-Hedbanz-Game/dp/B003AIM52A/ref=asc_df_B003AIM52A?mcid=9d4c7b066a97384db13c5b845c0c0426&tag=googshopuk-21&linkCode=df0&hvadid=697316272301&hvpos=&hvnetw=g&hvrand=3127525745372442187&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-420700901251&hvocijid=3127525745372442187-B003AIM52A-&hvexpln=0&gad_source=1&th=1)

- [operation](https://www.amazon.co.uk/Hasbro-Gaming-Classic-Operation-Game/dp/B01J3KRZRS/ref=asc_df_B01J3KRZRS?mcid=fbfd022a8f973d09a1b2bc5985ea4132&th=1&psc=1&tag=googshopuk-21&linkCode=df0&hvadid=696350735931&hvpos=&hvnetw=g&hvrand=13565994558038334510&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007448&hvtargid=pla-426288045555&psc=1&hvocijid=13565994558038334510-B01J3KRZRS-&hvexpln=0&gad_source=1)

- [battleship](https://www.argos.co.uk/product/9614686?utm_custom6=LIA&deeplink=true&gclsrc=aw.ds&&cmpid=GS001&_$ja=tsid:59130|acid:289-152-2757|cid:599609992|agid:24126986217|tid:pla-1079432869632|crid:94168542777|nw:g|rnd:5904851900067667145|dvc:c|adp:|mt:|loc:1007448&utm_source=Google&utm_medium=cpc&utm_campaign=599609992&utm_term=&utm_content=shopping&utm_custom1=24126986217&utm_custom2=289-152-2757&GPDP=true&gad_source=1&gad_campaignid=599609992&gbraid=0AAAAAD9II9nwZgKxpTqC-p5KWRqk41VmO&gclid=CjwKCAjwisnGBhAXEiwA0zEOR_7v7MPslnGRsUFu1Wp9usVD-pgBYCMO_mbXraAuFGl4XTeL4T9mhBoC4sQQAvD_BwE)


## Acknowledgements

Special thanks to Code Institute for foundational tutorials and project guidance. I followed the walkthrough tutorials to help create this website.

Inspired by:
- [Zatu Games](https://www.board-game.co.uk/)
- [Big Potato Games](https://bigpotato.co.uk/)
- [Board Game Geek](https://boardgamegeek.com/)

## Final Thoughts

Building Kingdom Of Games allowed me to create an online space where board game lovers can come together, explore a wide variety of games, and bring joy to their gatherings, whether they're 5 or 55 years old.
