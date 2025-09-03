# Telegram-bot-cobalt

[![version](https://img.shields.io/badge/Version-0.1.0-red?style=flat&logo=github&logoColor=white)]()
[![GitHub](https://img.shields.io/badge/Used-Cobalt%20API-blue?style=flat&logo=github&logoColor=white)](https://github.com/imputnet/cobalt)

A Telegram bot for downloading media from various sources.



## Usage

### Running the bot with Docker Compose

1. Open or create the `docker-compose.yml` file:

    ```
    nano docker-compose.yml
    ```

2. Paste the content from the [docker-compose.yml](https://gitlab.com/Kovalssky/telegram-bot-cobalt/-/raw/master/docker_compose.yml) file.

3. Start the bot by running:

    ```
    docker compose up -d
    ```

---
## Language Support

Currently, the bot supports only **Russian** and **English** languages.

The bot uses automatic localization selection, meaning it adapts to the user's device language automatically by leveraging Telegram's built-in features.

Localization is implemented using the **Fluent** framework, providing flexible and convenient translation management.

New languages can be added by creating translation files inside the `locales` folder.

Examples of translation files can be copied and adapted from existing completed translations.

---
> The bot is currently in alpha version and will receive frequent updates.
