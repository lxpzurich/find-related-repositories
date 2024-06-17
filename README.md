# Find Related Repos (Stargazer Analyzer)

Handy, simple tool for the discovery of repositories related to given Github repo. 
Helps answering the question "Are there repos that I am missing out on"?
"Find Related Repos" analyzes the most recent stargazers of a given GitHub repository and provides a ranked list of repositories similar to it based on user interest.
Using a GitHub API key is optional but you won't get far with unauthenticated requests, so using an API key is recommended.

## Features

- Fetch the most recent stargazers of a GitHub repository.
- Retrieve all starred repositories for each stargazer.
- Generate a ranked list of similar repositories.
- Save the results to a CSV file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/stargazer-analyzer.git
    cd stargazer-analyzer
    ```

2. Install the required packages:
    ```sh
    pip install python-dotenv requests
    ```

3. Create a `.env` file with your GitHub API key:
    ```sh
    GITHUB_API_KEY=your_github_api_key
    ```
    
## Usage

Run the script and follow the prompts:
```sh
python find_related_repos.py
```

You will be asked to input the repository name (e.g., DePayFi/widgets) and the number of users to fetch. The user default is 30.

## Output Example

- Input repository: [DePayFi/widgets](https://github.com/DePayFi/widgets)
- CSV Output:
    ```csv
    repo,user_count,stars,description,link
    DePayFi/widgets,17,87,💸 Payments directly into your wallet. DePay simplifies and improves Web3 Payments with the power of DeFi. Accept any token with on-the-fly conversion and state-of-the-art widgets.,https://github.com/DePayFi/widgets
    abi/screenshot-to-code,6,53723,Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue),https://github.com/abi/screenshot-to-code
    OneKeyHQ/app-monorepo,4,1841,"Secure, open source and community driven crypto wallet runs on all platforms and trusted by millions.",https://github.com/OneKeyHQ/app-monorepo
    telegraf/telegraf,3,7868,Modern Telegram Bot Framework for Node.js,https://github.com/telegraf/telegraf
    nocobase/nocobase,3,10672,"NocoBase is a scalability-first, open-source no-code/low-code platform for building business applications and enterprise solutions.",https://github.com/nocobase/nocobase
    assafelovic/gpt-researcher,3,12772,GPT based autonomous agent that does online comprehensive research on any given topic,https://github.com/assafelovic/gpt-researcher
    danielmiessler/fabric,3,16476,fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere.,https://github.com/danielmiessler/fabric
    Lissy93/web-check,3,19493,🕵️‍♂️ All-in-one OSINT tool for analysing any website,https://github.com/Lissy93/web-check
    andrewyng/translation-agent,3,2933,,https://github.com/andrewyng/translation-agent
    yagop/node-telegram-bot-api,2,8066,Telegram Bot API for NodeJS,https://github.com/yagop/node-telegram-bot-api
    MoralisWeb3/unity-web3-game-kit,2,522,Unity Web3 Game Kit is the fastest way to connect and build games for Web3. It provides a single workflow for building high performance dapps. Fully compatible with your favourite platform.,https://github.com/MoralisWeb3/unity-web3-game-kit
    run-llama/llama_index,2,32703,LlamaIndex is a data framework for your LLM applications,https://github.com/run-llama/llama_index
    nomic-ai/gpt4all,2,65855,gpt4all: run open-source LLMs anywhere,https://github.com/nomic-ai/gpt4all
    trader-xyz/nft-swap-sdk,2,217,Ethereum's missing p2p NFT and token swap library for web3 developers. Written in TypeScript. Powered by 0x.,https://github.com/trader-xyz/nft-swap-sdk
    DePayFi/web3-client,2,10,🌐 A web3 client to fetch blockchain data just like you are used to with HTTP clients.,https://github.com/DePayFi/web3-client
    bitrise-steplib/steps-google-play-deploy,2,52,,https://github.com/bitrise-steplib/steps-google-play-deploy
    bitrise-steplib/steps-set-xcode-build-number,2,7,Sets the Build Number to the specified value in the Info.plist file for the next build,https://github.com/bitrise-steplib/steps-set-xcode-build-number
    callstack/react-native-builder-bob,2,2674,👷‍♂️ Simple set of CLIs to scaffold and build React Native libraries for different targets,https://github.com/callstack/react-native-builder-bob
    tinacms/tinacms,2,11382,A fully open-source headless CMS that supports Markdown and Visual Editing,https://github.com/tinacms/tinacms
    OpenBMB/MiniCPM-V,2,7278,MiniCPM-Llama3-V 2.5: A GPT-4V Level Multimodal LLM on Your Phone,https://github.com/OpenBMB/MiniCPM-V
    it-ebooks-0/geektime-books,2,8486,:books: 极客时间电子书,https://github.com/it-ebooks-0/geektime-books
    lencx/ChatGPT,2,51415,"🔮 ChatGPT Desktop Application (Mac, Windows and Linux)",https://github.com/lencx/ChatGPT
    opentofu/opentofu,2,21436,OpenTofu lets you declaratively manage your cloud infrastructure.,https://github.com/opentofu/opentofu
    termuxprofessor/Telegram-Scraper-Adder,2,366,Python Script For Scarpe Telegram Members From Another Group And Add That Members To Your Group.,https://github.com/termuxprofessor/Telegram-Scraper-Adder
    BuilderIO/micro-agent,2,1080,An AI agent that writes (actually useful) code for you,https://github.com/BuilderIO/micro-agent
    BasedHardware/Friend,2,1876,AI wearable necklace,https://github.com/BasedHardware/Friend
    karpathy/nanoGPT,2,33890,"The simplest, fastest repository for training/finetuning medium-sized GPTs.",https://github.com/karpathy/nanoGPT
    expo/expo,2,30461,"An open-source framework for making universal native apps with React. Expo runs on Android, iOS, and the web.",https://github.com/expo/expo
    m-bain/whisperX,2,9723,WhisperX:  Automatic Speech Recognition with Word-level Timestamps (& Diarization),https://github.com/m-bain/whisperX
    ItzCrazyKns/Perplexica,2,9788,Perplexica is an AI-powered search engine. It is an Open source alternative to Perplexity AI,https://github.com/ItzCrazyKns/Perplexica
    VikParuchuri/marker,2,12745,Convert PDF to markdown quickly with high accuracy,https://github.com/VikParuchuri/marker
    goldmansachs/gs-quant,2,3091,Python toolkit for quantitative finance,https://github.com/goldmansachs/gs-quant
    miurla/morphic,2,4814,An AI-powered search engine with a generative UI,https://github.com/miurla/morphic
    adrianhajdin/ai_saas_app,2,894,"Build a REAL Software-as-a-Service app with AI features and payments & credits system that you might even turn into a side income or business idea using Next.js 14, Clerk, MongoDB, Cloudinary AI, and Stripe.",https://github.com/adrianhajdin/ai_saas_app
    immense/Remotely,2,4252,"A remote control and remote scripting solution, built with .NET 8, Blazor, and SignalR.",https://github.com/immense/Remotely
    apache/hertzbeat,2,5052,"Apache HertzBeat(incubating) is a real-time monitoring system with agentless, performance cluster, prometheus-compatible, custom monitoring and status page building capabilities.",https://github.com/apache/hertzbeat
    BasedHardware/OpenGlass,2,2496,Turn any glasses into AI-powered smart glasses,https://github.com/BasedHardware/OpenGlass
    truefoundry/cognita,2,2812,"RAG (Retrieval Augmented Generation) Framework for building modular, open source applications for production by TrueFoundry ",https://github.com/truefoundry/cognita
    vectorisvector/Polaris,2,424,,https://github.com/vectorisvector/Polaris
    puppeteer/puppeteer,2,87432,Node.js API for Chrome ,https://github.com/puppeteer/puppeteer
    DePayFi/web3-wallets,2,66,👛 One-Stop-Shop JavaScript library to integrate various web3 crypto wallets and multiple blockchains at once with a single interface.,https://github.com/DePayFi/web3-wallets
    NomicFoundation/hardhat,2,6937,"Hardhat is a development environment to compile, deploy, test, and debug your Ethereum software. ",https://github.com/NomicFoundation/hardhat
    twitter/the-algorithm,2,61596,Source code for Twitter's Recommendation Algorithm,https://github.com/twitter/the-algorithm
    entropy-research/Devon,2,2070,Devon: An open-source pair programmer,https://github.com/entropy-research/Devon
    (...)
    ```
