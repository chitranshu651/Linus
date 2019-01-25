package core;

import com.google.gson.JsonElement;
import com.jfoenix.controls.*;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;

import ai.api.AIConfiguration;
import ai.api.AIDataService;
import ai.api.model.AIRequest;
import ai.api.model.AIResponse;

import java.lang.reflect.Field;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

public class Controller {

    @FXML
    private JFXButton goButton;

    @FXML
    private JFXTextField inputField;

    @FXML
    private JFXListView list;

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
            if(inputField.getText().equals("")) {
                return;
            }
            //setting GOOGLE_APPLICATION_CREDENTIALS variable
//            setEnv("GOOGLE_APPLICATION_CREDENTIALS", "/home/iosdev747/Downloads/creds.json");
//            voiceThread = new Thread(new Recognizer());
//            voiceThread.start();
            AIConfiguration configuration = new AIConfiguration("c3a31db2f9bc467abebad1e364b8ff9f");

            AIDataService dataService = new AIDataService(configuration);
            System.out.print("START ");
            try {
                AIRequest request = new AIRequest(inputField.getText());
                //random unique sessionID
                request.setSessionId("1337");
                AIResponse response = dataService.request(request);
                System.out.println("\nSend Request: "+inputField.getText());
                System.out.println("session:"+response.getSessionId());
                if (response.getStatus().getCode() == 200) {
                    String action = response.getResult().getAction();
                    System.out.println("Action: "+action);
                    System.out.println("Speech: "+response.getResult().getFulfillment().getSpeech());
                    if(!response.getResult().getFulfillment().getSpeech().isEmpty()){
                        list.getItems().add(response.getResult().getFulfillment().getSpeech());
                    }else{
                        list.getItems().add(response.getResult().getAction());
                        HashMap<String, JsonElement> hashMap = response.getResult().getParameters();
                        Object[] arrays = hashMap.keySet().toArray();
                        for (Object o:arrays) {
                            System.out.println("" + hashMap.get(o));
                            list.getItems().add(o+":"+hashMap.get(o));
                        }
                        if(response.getResult().getAction().equals("cda") || response.getResult().getAction().equals("cdr")) {
                            StringJoiner joiner = new StringJoiner("/");
                            for (Object o:hashMap.keySet().toArray()) {
                                joiner.add(hashMap.get(o).toString()).add("/");
                            }
                            return;
                        }
                        System.out.println("output:" + response.getResult().getAction());
                    }
                } else {
                    System.err.println(response.getStatus().getErrorDetails());
                }
            } catch (Exception ex) {
                ex.printStackTrace();
            }
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

    public void updateGUI() {
        System.out.println("updating GUI");
        //// TODO: 26/1/19 update GUI, read data from output from python's o/p
    }

}
