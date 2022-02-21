package exam01;

public class Char01 {
	public static void main(String[] args) {
		Student studyStudent = new Student("박하은");
		System.out.println(studyStudent.name);
		
		Student sleepStudent = new Student();
		sleepStudent.name = "박하영";
		System.out.println(sleepStudent.name);
	}
}