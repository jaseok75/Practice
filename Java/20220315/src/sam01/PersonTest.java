package sam01;

public class PersonTest {
	public static void main(String[] args) {
		Person person1 = new Person("박하은", 1111);
		System.out.println("이름: " + person1.name);
		System.out.println("번호: " + person1.number);
	}
}
