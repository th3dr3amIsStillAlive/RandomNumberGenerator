# RandomNumberGenerator
A very simple random number generator built for Windows. 


Either just download the ready built executable for Windows, or build it yourself:

1. ` git clone https://github.com/th3dr3amIsStillAlive/RandomNumberGenerator`
2. ` cd RandomNumberGenerator `
3. ` pip install -r requirements.txt `
4. Build the executable: ` pyinstaller --onefile --windowed --icon=icon.ico --name=RandomNumberGenerator .\rng.py `
5. Then you'll find the `RandomNumberGenerator.exe` in the `dist` directory