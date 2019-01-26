package core;

import core.watchdogs.ErrorWatchDog;
import core.watchdogs.OutputWatchDog;
import javafx.fxml.Initializable;

import java.net.URL;
import java.nio.file.Paths;
import java.util.ResourceBundle;

public class Bot implements Runnable {

    Bot() { (new Thread(this)).start(); }

    @Override
    public void run() {
        DAO.pwd = Paths.get(".");
        System.out.println(DAO.pwd.toString());
        new OutputWatchDog();
        new ErrorWatchDog();
    }
}
