
public class ArrayTest {
	public static void main(String[] args) {
		int[] arr1 = new int[5];
		//int[] arr2 = arr1; // 얕은 복사 (주소 참조)
		int[] arr2 = new int[5];
		//int[] arr2 = {10, 20, 35, 30, 45};
		arr1[0] = 10;
		arr1[1] = 20;
		arr1[2] = 25;
		arr1[3] = 30;
		arr1[4] = 45;
		
		for (int i = 0; i < arr1.length; i++) {
			arr2[i] = arr1[i];
		}
		
		arr1[0] = 100;
		
		for (int i = 0; i < arr1.length; i++) {
			System.out.println(arr1[i]);
		}
		
		System.out.println("========================");
		
		for (int i = 0; i < arr2.length; i++) {
			System.out.println(arr2[i]);
		}
	}
}