package core;

import java.nio.file.Path;

/**
 * DAO - Data Access Object
 * Class used for accessing static variables between multiple classes
 */

public class DAO {
    static String voiceOutput;
    public static Controller controller;
    static Path pwd; //for sending path to commands
    static Output output;
}
