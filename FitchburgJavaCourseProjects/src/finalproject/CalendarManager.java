package finalproject;

/**
 * @author Prashanthi sudha kosgi
 * date :06/23/2017.
 * 
 */
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class CalendarManager {

	public void saveCalendarEntry(int day, int month, int year, String entry) {
		String[] entries = null;

		String fileName = getFileName(month, year);

		File file = new File(fileName);
		if (file.exists() && !file.isDirectory())
			entries = getEntries(fileName);

		if (entries == null)
			entries = new String[31];

		entries[day - 1] = entry;

		try {
			ObjectOutputStream writer = new ObjectOutputStream(new FileOutputStream(fileName));
			writer.writeObject(entries);
			writer.close();
		} catch (IOException exception) {
			exception.printStackTrace();
		}
	}

	/**
	 * Get the calendar entry
	 * @param day
	 * @param month
	 * @param year
	 * @return String
	 */
	public String retrieveCalendarEntry(int day, int month, int year) {
		String fileName = getFileName(month, year);
		File file = new File(fileName);
		if (file.exists() && !file.isDirectory()) {
			String[] entries = getEntries(fileName);
			if (entries != null) {
				String entry = entries[day - 1];
				if (entry != null)
					return entry;
				else
					return "No Such Entry";
			} else {
				return "No Such Entry";
			}
		}
		return "No Such Entry";
	}

	/**
	 * Get entries from the file to String Array
	 * @param fileName
	 * @return
	 */
	private String[] getEntries(String fileName) {
		try {
			ObjectInputStream reader = new ObjectInputStream(new FileInputStream(fileName));
			String[] entries = (String[]) reader.readObject();
			reader.close();
			return entries;
		} catch (IOException exception) {
			exception.printStackTrace();
		} catch (ClassNotFoundException exception) {
			exception.printStackTrace();
		}
		return null;
	}

	/**
	 * Create file name using month and year
	 * @param month
	 * @param year
	 * @return
	 */
	private String getFileName(int month, int year) {
		String fileName = year + "-";
		if (month < 10)
			fileName += "0" + month;
		else
			fileName += month;
		fileName += ".txt";
		return fileName;
	}
}
