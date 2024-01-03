# RandomNumberGenerator
A very simple random number generator built for Windows using PyQt5. 

## Usage
You can download the ready-built executable from the [Releases](https://github.com/th3dr3amIsStillAlive/RandomNumberGenerator/releases) page. Be aware that Windows SmartScreen might prompt a warning as the executable is not signed with a certificate. To run anyway, click "More Info" and then "Run Anyway". If you prefer, you can build it from source as follows:

### Building from Source
1. Clone the repository: ` git clone https://github.com/th3dr3amIsStillAlive/RandomNumberGenerator`
2. Navigate to the project directory: ` cd RandomNumberGenerator `
3. Install dependencies: ` pip install -r requirements.txt `
4. Build the executable: ` pyinstaller --onefile --windowed --icon=icon.ico --name=RandomNumberGenerator .\rng.py `
5. Find the `RandomNumberGenerator.exe` in the `dist` directory