import java.io.*;

public class Homework2 {

	public static void main(String[] args) {
		try {
			File file = new File ("property.html");
			BufferedWriter writer = new BufferedWriter(new FileWriter(file));
			//writer.write("sample text");
			writer.write("<head>");
			writer.write("<meta charset=\"UTF-8\"/>");
			writer.write("<style>");
			writer.write("table {border-collapse: collapse; width: 100%; }\r\n");
			writer.write("th, td { border:solid 1px #000; }");
			writer.write("</style>");
			
			writer.write("<body><h1>자바 환경정보</h1><table>");
			writer.write("<th>키</th><th></th>");
			for (Object k : System.getProperties().keySet()) {
				String key = k.toString();
				String value = System.getProperty(key);
				writer.write("<tr>");
				writer.write("<td>"+key+"</td>"+"<td>"+value+"</td></tr>");
			}
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
