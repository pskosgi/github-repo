package dao;

import bean.PatientData;

public class PatientDAO {
	
	public PatientData getPatentDataByName(String name){
		
		//dummy data.
		// to get real data, call the DataBase Using JDBC
		PatientData pd = new PatientData();
		pd.setAddress("25 ABC, TX , US");
		pd.setFirstName("Amber");
		pd.setLastName("Light");
		pd.setPatentPrimaryDoctor("Dr. Joseph");
		
		return pd;
		
	}

}
