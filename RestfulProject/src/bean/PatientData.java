package bean;

public class PatientData {
	
	public int id;
	
	private String firstName;
	
	private String lastName;
	
	private String patentPrimaryDoctor;
	
	private String address;
	
	private int phoneNumber;
	
	private String recordNumber;
	
	//TODO data more
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getPatentPrimaryDoctor() {
		return patentPrimaryDoctor;
	}

	public void setPatentPrimaryDoctor(String patentPrimaryDoctor) {
		this.patentPrimaryDoctor = patentPrimaryDoctor;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public int getPhoneNumber() {
		return phoneNumber;
	}

	public void setPhoneNumber(int phoneNumber) {
		this.phoneNumber = phoneNumber;
	}

	public String getRecordNumber() {
		return recordNumber;
	}

	public void setRecordNumber(String recordNumber) {
		this.recordNumber = recordNumber;
	}


	
}
