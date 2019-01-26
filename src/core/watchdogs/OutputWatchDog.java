package core.watchdogs;

import core.DAO;
import core.FileIO;

import java.io.IOException;
import java.nio.file.*;

/**
 * Watchdog on output from python, will be used for updating GUI
 */
public class OutputWatchDog implements Runnable {

    public OutputWatchDog() { (new Thread(this)).start(); }

    @Override
    public void run() {
        Path path = DAO.pythonPath;
        System.out.println("O:"+path);
        try (final WatchService watchService = FileSystems.getDefault().newWatchService()) {
            final WatchKey watchKey = path.register(watchService, StandardWatchEventKinds.ENTRY_MODIFY);
            while (true) {
                final WatchKey wk = watchService.take();
                System.out.println("Output File Register at: "+path.toString() + "/output.txt");
                for (WatchEvent<?> event : wk.pollEvents()) {
                    //we only register "ENTRY_MODIFY" so the context is always a Path.
                    final Path changed = (Path) event.context();
                    System.out.println(changed);
                    if (changed.endsWith("output.txt")) {
                        System.out.println("output has changed");
                        FileIO.readJSONFrom(path.toString() + "/output.txt");
                        core.DAO.controller.updateGUI();
                    }
                }
                // reset the key
                boolean valid = wk.reset();
                if (!valid) {
                    System.out.println("Key has been unregistered");
                }
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
