package core.watchdogs;

import core.FileIO;

import java.io.IOException;
import java.nio.file.*;

/**
 * Watchdog on output from python, will be used for updating GUI
 */
public class OutputWatchDog implements Runnable {

    OutputWatchDog() { (new Thread(this)).start(); }

    @Override
    public void run() {
        String outputFilePath = "location_of_output_from_python"; //not decided yet, not include name of file, filename = output
        Path path = Paths.get(outputFilePath);
        System.out.println(path);
        try (final WatchService watchService = FileSystems.getDefault().newWatchService()) {
            final WatchKey watchKey = path.register(watchService, StandardWatchEventKinds.ENTRY_MODIFY);
            while (true) {
                final WatchKey wk = watchService.take();
                System.out.println(path.toString() + "/output");
                for (WatchEvent<?> event : wk.pollEvents()) {
                    //we only register "ENTRY_MODIFY" so the context is always a Path.
                    final Path changed = (Path) event.context();
                    System.out.println(changed);
                    if (changed.endsWith("output")) {
                        System.out.println("output has changed");
                        FileIO.readJSONFrom(path.toString() + "/output");
                        core.DAO.controller.updateGUI();
                    }
                }
                // reset the key
                boolean valid = wk.reset();
                if (!valid) {
                    System.out.println("Key has been unregisterede");
                }
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
