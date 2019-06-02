package core;

import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * DAO - Data Access Object
 * Class used for accessing static variables between multiple classes
 */

public class DAO {
    static String voiceOutput;
    public static Controller controller;
    static Path pwd; //for sending path to commands
    static Output output;
    public static final Path pythonPath = Paths.get("/home/iosdev747/Desktop/Linus/Linus");
    public static final String api_ai_clientAccessToken = "c3a31db2f9bc467abebad1e364b8ff9f";
}
