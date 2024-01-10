# Aura-DesktopVoiceAssistant

Aura is a desktop voice assistant built in Python that allows users to interact with their computer using voice commands. The assistant is designed to perform various tasks such as opening applications, providing information, and more.

Features:

Greetings and Introduction:

Upon starting, Aura greets the user based on the current time (morning, afternoon, or evening).
Introduces itself as "Aura" and asks how it can help.

Wikipedia Search:

If the user mentions "Wikipedia" in their query, Aura searches Wikipedia for information and speaks a summary.

Web Browsing:

Opens various websites based on user commands:
YouTube
Google
GeeksforGeeks (GFG)
LeetCode
CodeChef
ChatGPT by OpenAI

Music Playback:

Plays music from a specified directory (D:\songs) by opening the first song in the directory.

Time Inquiry:

Tells the current time when the user asks for it.

Application Opening:

Opens specific applications based on user commands:
Visual Studio Code (VS Code)
Microsoft Word
Application Closing:

Closes applications based on user commands. The function close_application tries to terminate a running application process.

Exiting the Assistant:

If the user says "quit," Aura thanks the user and exits the program.
