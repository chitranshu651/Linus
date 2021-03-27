package core;

import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FileIO {

    /**
     * read json file and store in Output class instance.
     * @param file Path with name of json file.
     */
    public static void readJSONFrom(String file) {
        //JSON parser object to parse read file
        Gson gson = new Gson();

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            DAO.output = gson.fromJson(br, Output.class);
            Files.delete(Paths.get(file)); //delete file after reading...
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static String readError(String fileName) {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String result = br.readLine();
            Files.delete(Paths.get(fileName));
            return result;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return "NULL:FUNCTION FAILS :'(";
    }

}
