package exam01;

public class Student {
	public String name;
	
	// 기본 생성자
	public Student() {
		System.out.println("학생 생성자가 호출되어짐");
	}
	
	// 매개변수를 갖는 생성자
	public Student(String name) {
		System.out.println("이름 파라미터를 갖는 학생 생성자가 호출되어짐");
		this.name = name;
	}
}
