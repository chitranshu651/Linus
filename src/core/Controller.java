package core;

import com.jfoenix.controls.*;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;

import java.lang.reflect.Field;
import java.util.Map;

public class Controller {

    @FXML
    private JFXButton goButton;

    @FXML
    private JFXTextField inputField;

    private boolean isProcessing = false;
    private Thread voiceThread;

    @FXML
    public void onGoAction(ActionEvent actionEvent) {
        System.out.println("action Running");
        if(isProcessing) {
            isProcessing = !isProcessing;
            if(voiceThread.isAlive()) {
                voiceThread.stop();
            }
            goButton.setText("Go");
        }
        else {
            isProcessing = !isProcessing;
//            if(inputField.getText().equals("")) {
//                return;
//            }
            //setting GOOGLE_APPLICATION_CREDENTIALS variable
            setEnv("GOOGLE_APPLICATION_CREDENTIALS", "/home/iosdev747/Downloads/creds.json");
            voiceThread = new Thread(new Recognizer());
            voiceThread.start();
            goButton.setText("Stop");
        }
    }

    /**
     * Method to set Environment Variable
     * @param key environment variable name
     * @param value environment variable value
     */
    public static void setEnv(String key, String value) {
        try {
            Map<String, String> env = System.getenv();
            Class<?> cl = env.getClass();
            Field field = cl.getDeclaredField("m");
            field.setAccessible(true);
            Map<String, String> writableEnv = (Map<String, String>) field.get(env);
            writableEnv.put(key, value);
        } catch (Exception e) {
            throw new IllegalStateException("Failed to set environment variable", e);
        }
    }
}
