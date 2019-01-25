package core;

import com.jfoenix.controls.*;
import javafx.fxml.FXML;

public class Controller {

    @FXML
    private JFXButton goButton;

    @FXML
    private JFXTextField inputField;

    private boolean isProcessing = false;
    private Thread voiceThread;

    public void action() {
        if(isProcessing) {
            isProcessing = !isProcessing;
            if(voiceThread.isAlive()) {
                voiceThread.stop();
            }
            goButton.setText("Go");
        }
        else {
            isProcessing = !isProcessing;
            if(inputField.getText().equals("")) {
                return;
            }
            voiceThread = new Thread(new Recognizer());
            voiceThread.start();
            goButton.setText("Stop");
        }
    }
}
