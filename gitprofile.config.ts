// gitprofile.config.js

const config = {
  github: {
    username: 'Felix-Helleckes', // Your GitHub org/user name. (Required)
  },
  projects: {
    github: {
      display: true,
      header: 'My personal Projects',
      mode: 'automatic',
      automatic: {
        sortBy: 'stars', // stars | updated
        limit: 4, // How many projects to display.
        exclude: {
          forks: false,
          projects: [],
        },
      },
    },
    external: {
      header: 'Past permanent positions',
      projects: [
        {
          title: 'Bike24',
          description:
            'Automated a Supply Chain Management solution for Bike24 based on SAP S/4HANA. Also worked with their e-commerce platform and automated various user flows with Playwright and Locust for performance testing.',
          imageUrl: 'https://s3-eu-west-1.amazonaws.com/tpd/logos/5f7727eeff11cd000138c964/0x0.png',
          link: 'https://www.bike24.de/',
        },
        {
          title: 'Peek & Cloppenburg Web Apps',
          description:
            'Peek & Cloppenburg is a German fashion retailer founded in 1869. With a large workforce there were many internal projects which we developed. I also worked in e-commerce development and automated many user flows with WebdriverIO and Locust.',
          imageUrl: 'https://play-lh.googleusercontent.com/yycoMy1dTRJMFbwyvIpctd44_T7MSvZF-oQ9jnrPDdzqJad2Lirrvjep3aLpx4D8_pQ',
          link: 'https://www.peek-cloppenburg.de/',
        },
        {
          title: 'KFW',
          description:
            'KfW, or Kreditanstalt für Wiederaufbau, is a German development bank. It is owned by the German government and provides loans and other financial services to businesses, governments, and individuals. KfW\'s main focus is on promoting economic development and social welfare in Germany',
          imageUrl: 'https://www.kfw-ipex-bank.de/Techn-Medien/Logos/Social-Media/KfW_IPEX_Logo_180x180px.png',
          link: 'https://www.kfw.de/kfw.de.html',
        },
        {
          title: 'Bega - The Good Light',
          description:
            'The bega connect gateway is a smart home gateway that supports Zigbee and DALI. It allows you to connect and control Zigbee and DALI devices with your smartphone or tablet.',
          imageUrl: 'https://image.winudf.com/v2/image1/ZGUuYmVnYS5iZWdhY29ubmVjdF9pY29uXzE2MTc5NjQwMTFfMDky/icon.png?w=184&fakeurl=1',
          link: 'https://connect.bega.com/en',
        },
        {
          title: 'Migros App',
          description:
            'Migros Genossenschaft is the largest Swiss retailer and one of the 40 largest retailers worldwide. Within the group, almost all relevant retail services are offered. With its restaurants, for example, Migros is one of the largest gastronomy companies in Switzerland. In addition to grocery stores, it also has DIY stores, electronics stores, sporting goods stores and furniture stores under its roof.',
          imageUrl: 'https://corporate.migros.ch/_next/static/media/mLogo.abe368b1.svg',
          link: 'https://grandcentrix.net/de/references/migros/',
        },
        {
          title: 'Leica Camera App',
          description:
            'The first almost 2 years at Grandcentrix I worked on the Leica camera app. I created a test concept for various cameras and a wide portfolio of Android and iOS versions. In addition, I managed the entire test process in Scrum, partly also with external service providers (personnel responsibility).',
          imageUrl: 'https://leica-camera.com/themes/custom/leica_redesign_theme/logo.svg',
          link: 'https://grandcentrix.net/de/references/leica',
        },
      ],
    },
  },
  seo: {
    title: 'Felix Helleckes – QA & Test Automation Engineer (Germany)',
    description: 'Felix Helleckes — QA & Test Automation Engineer based in Germany, covering the DACH region and remote work. Playwright, WebdriverIO, Selenium, Locust, CI/CD.',
    imageURL: 'https://github.com/Felix-Helleckes.png',
  },
  social: {
    linkedin: 'felix-helleckes-758529202/',
    //twitter: '',
    //mastodon: 'arifszn@mastodon.social',
    //facebook: '',
    //instagram: '',
    youtube: 'TheEfficientDev', // example: 'pewdiepie'
    //dribbble: '',
    //behance: '',
    medium: 'felix-helleckes',
    dev: 'felix-helleckes',
    stackoverflow: '15774380/felix-helleckes', // example: '1/jeff-atwood'
    //skype: '',
    //telegram: '',
    website: 'https://felix-helleckes.github.io/',
    //phone: '+491758316710',
    email: 'f.helleckes@proton.me',
  },
  resume: {
    fileUrl: '', // Empty fileUrl will hide the `Download Resume` button.
  },
  skills: [
    'claude',
    'openclaw',
    'n8n Workflow Automation (json, javascript)',
    'Playwright',
    'Webdriver.io',
    'Selenium/Appium',
    'locust.io',
    'SAP S/4HANA Test Automation Tool',
    'Postman',
    'Jenkins CI/CD',
    'Docker',
    'Testrail',
    'Test Management in Scrum Workflow',
    'Testmo'
  ],
  experiences: [
      {
      company: 'Bike24',
      position: 'QA-Engineer',
      from: 'Nov 2023',
      to: 'Oct 2025',
      companyLink: 'https://www.bike24.de/',
    },
    {
      company: 'Peek & Cloppenburg (Fashion Digital)',
      position: 'Associate-Manager:Quality Assurance',
      from: 'Dec 2021',
      to: 'Oct 2023',
      companyLink: 'https://www.peek-cloppenburg.de/',
    },
    {
      company: 'Ampada',
      position: 'QA-Engineer',
      from: 'Feb 2021',
      to: 'Aug 2021',
      companyLink: 'https://grandcentrix.net/de/',
    },
    {
      company: 'Grandcentrix',
      position: 'QA-Tester',
      from: 'Feb 2018',
      to: 'Feb 2021',
      companyLink: 'https://grandcentrix.net/de/',
    },
  ],
  /* certifications: [
    {
      name: 'Lorem ipsum',
      body: 'Lorem ipsum dolor sit amet',
      year: 'March 2022',
      link: 'https://example.com'
    },
  ], */
  education: [
    {
      institution: 'Hönne Berufskolleg Menden',
      degree: 'Fachabitur & Vocational Training',
      from: '2009',
      to: '2014',
    },
    // {
    //   institution: 'Institution Name',
    //   degree: 'Degree',
    //   from: '2012',
    //   to: '2014',
    // },
  ],

  // Display blog posts from your medium or dev account. (Optional)
  blog: {
    source: 'medium', // medium | dev
    username: 'felix-helleckes', // to hide blog section, keep it empty
    limit: 10, // How many posts to display. Max is 10.
  },
  googleAnalytics: {
    id: 'G-3JBR11V8QH', // GA3 tracking id/GA4 tag id UA-XXXXXXXXX-X | G-XXXXXXXXXX
  },
  // Track visitor interaction and behavior. https://www.hotjar.com
  hotjar: {
    id: '',
    snippetVersion: 6,
  },
  themeConfig: {
    defaultTheme: 'black',

    // Hides the switch in the navbar
    // Useful if you want to support a single color mode
    disableSwitch: false,

    // Should use the prefers-color-scheme media-query,
    // using user system preferences, instead of the hardcoded defaultTheme
    respectPrefersColorScheme: false,

    // Hide the ring in Profile picture
    hideAvatarRing: false,

    // Available themes. To remove any theme, exclude from here.
    themes: [
      'light',
      'black',
      'coffee',
      'lemonade',
      //'dracula',
      //'dark',
      // 'cupcake',
      // 'bumblebee',
      // 'emerald',
      // 'corporate',
      'synthwave',
      // 'retro',
      // 'cyberpunk',
      // 'valentine',
      // 'halloween',
      // 'garden',
      // 'forest',
      // 'aqua',
      // 'lofi',
      // 'pastel',
      // 'fantasy',
      // 'wireframe',
      // 'luxury', 
      // 'cmyk',
      // 'autumn',
      //'business',
      //'acid',
      //'night',
      //'winter',
      //'procyon',
    ],

    // Custom theme
    customTheme: {
      primary: '#fc055b',
      secondary: '#219aaf',
      accent: '#e8d03a',
      neutral: '#2A2730',
      'base-100': '#E3E3ED',
      '--rounded-box': '3rem',
      '--rounded-btn': '3rem',
    },
  },

  // Optional Footer. Supports plain text or HTML.
  footer: `Made with <a 
      class="text-primary" href="https://react.dev/"
      target="_blank"
      rel="noreferrer"
    >React.dev</a> and ❤️`,
};

export default config;
