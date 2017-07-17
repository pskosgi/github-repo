package finalproject;
/**
 * @author Prashanthi sudha kosgi
 * date :06/23/2017.
 * 
 */

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;

public class UserInterface extends JFrame {
	private static final long serialVersionUID = 1L;
	private CalendarManager manager;
	private JButton save, retrieve;
	private JTextArea entryData;
	private JLabel status;
	private JComboBox<Integer> days, months, years;

	// Constructor 
	public UserInterface() {
		setTitle("Calendar Manager");
		setSize(600, 400);
		setLayout(new FlowLayout());

		manager = new CalendarManager();

		save = new JButton("Save");
		retrieve = new JButton("Retrieve");
		entryData = new JTextArea(20, 30);

		Integer[] monthValues = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 };
		Integer[] yearValues = { 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 };
		Integer[] daysCount = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

		days = new JComboBox<Integer>();
		months = new JComboBox<Integer>(monthValues);
		years = new JComboBox<Integer>(yearValues);

		add(new JLabel("Please Select Date : "));
		add(new JLabel(" MONTH "));
		add(months);
		add(new JLabel(" DAY "));
		add(days);
		add(new JLabel(" YEAR "));
		add(years);

		for (Integer i = 1; i <= 31; i++)
			days.addItem(i);
		months.setSelectedIndex(0);

		months.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent event) {
				Integer selectedMonth = (Integer) months.getSelectedItem();
				Integer selectedYear = (Integer) years.getSelectedItem();
				int maximumDaysInMonth = daysCount[selectedMonth - 1];
				if ((selectedYear % 400 == 0) || ((selectedYear % 4 == 0) && (selectedYear % 100 != 0)))
					if (selectedMonth == 2)
						maximumDaysInMonth++;
				days.removeAllItems();
				for (Integer i = 1; i <= maximumDaysInMonth; i++)
					days.addItem(i);
			}
		});

		retrieve = new JButton("Retrieve");
		retrieve.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent event) {
				Integer selectedDay = (Integer) days.getSelectedItem();
				Integer selectedMonth = (Integer) months.getSelectedItem();
				Integer selectedYear = (Integer) years.getSelectedItem();

				entryData.setText(manager.retrieveCalendarEntry(selectedDay, selectedMonth, selectedYear));
				status.setVisible(false);
			}
		});
		add(retrieve);
		JLabel entriesTitle = new JLabel("Calendar Entries");
		entriesTitle.setPreferredSize(new Dimension(400, 20));
		add(entriesTitle);
		entryData = new JTextArea(10, 33);
		add(entryData);
		save = new JButton("Save");

		save.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent event) {
				Integer selectedDay = (Integer) days.getSelectedItem();
				Integer selectedMonth = (Integer) months.getSelectedItem();
				Integer selectedYear = (Integer) years.getSelectedItem();
				String entry = entryData.getText();

				manager.saveCalendarEntry(selectedDay, selectedMonth, selectedYear, entry);
				status.setVisible(true);
			}
		});
		add(save);

		status = new JLabel("Entry Saved");
		status.setVisible(false);
		status.setPreferredSize(new Dimension(400, 20));
		add(status);

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
	}

}
