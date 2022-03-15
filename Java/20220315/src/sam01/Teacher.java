package sam01;

public class Teacher extends Person {
	public String schoolName;
	public long number;
	
	public Teacher(String name, long number, String schholName, long t_number) {
		super(name, number);
		this.schoolName = schoolName;
		this.number = t_number;
	}
}
