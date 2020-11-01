# Streak Manager

A simple productivity tool that helps you keep a "streak" going by tracking your progress.

Streak Manager aims to be:

- Universal
- Portable
- Extensible

## 

## Tech Stack

This is a CLI tool written in Python; however, the client isn't the main focus here, rather it is the development of ththe underlying API aims to be both universal and portable, a client that is adhering to the API should be compatible with an `st_data.json` file which acts as the back-end that this client functions on. It's structure looks somewhat like this:

```json
{
  "user": {},
  "streaks": [
    {
      "name": "coding challenges",
      "type": "daily",
      "data": {}
    },
    {
      "name": "100 pushups",
      "type": "goal",
      "data": {}
    }
  ]
}
```

This file is read everytime the client runs and is updated whenever an operation is perfomed by the client, this file can be synced through any cloud service e.g. Dropbox, iCloud and be used across different `streak_manager`-compatible clients which I am planning to introduce gradually with the help of contributors, with this CLI Python Client acting as the basis for what a client should be able to do and what features should it offer, the means with which the client offers these features doesn't matter, It can be anything from a web-based drag & drop client to a speech-driven interaction through a smart watch, the only constraint is: All of them should produce the exact same `st_data.json` file to allow compatibility between all clients.

Keep in mind the `st_data.json` format is still being developed with plans for different types of streaks and ways to implement them, e.g. Some goals will require logging everyday and will count consecutive days of work, some will be a 1-time milestone that you just need to achieve once, some will be track amount of something you have done (hours spent coding, books read in a month etc..), there is alot of potential and the scope can grow dramatically with plans of implementing deadlines, calendar integration etc..

This project is aimed to introduce the concept of APIs (in its generic meaning) to newcomers; additionally, it serves as a great basis for new open-source students to practice on due to its simplicity of concept, structure and the extensibility that gives room for people adding their own commands and cmdlets, hence it could be viewed as a mere practice project as well.
