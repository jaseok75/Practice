package exam01;

public class ColledgeStudent {
	public String name;
	public int age;
	public String gender;
	public String department;
	
	public ColledgeStudent() {
		
	}
	
	public ColledgeStudent(String name) {
		this.name = name;
	}
	
	public ColledgeStudent(String name, int age) {
		//this.name = name;
		this(name);
		//this 생성자는 1번만 사용 가능
		this.age = age;
	}
	
	public ColledgeStudent(String name, int age, String gender) {
		//this.name = name;
		this(name);
		this.age = age;
		this.gender = gender;
	}
	
	public ColledgeStudent(String name, int age, String gender, String department) {
		this.name = name;
		this.age = age;
		this.gender = gender;
		this.department = department;
	}
	
	public ColledgeStudent(String name, String gender) {
		this.name = name;
		this.gender = gender;
	}
}
