package core;

import core.watchdogs.OutputWatchDog;
import javafx.fxml.Initializable;

import java.net.URL;
import java.util.ResourceBundle;

public class Bot implements Runnable, Initializable {

    Bot() { (new Thread(this)).start(); }

    @Override
    public void run() {

    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        new OutputWatchDog();
    }
}
