package servlet1;

import jakarta.servlet.*;
import jakarta.servlet.annotation.*;
import jakarta.servlet.http.*;
import java.io.IOException;
import java.util.*;

@WebServlet("/students")
public class StudentServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Create a list of student names
        List<String> students = new ArrayList<>();
        students.add("Alice");
        students.add("Bob");
        students.add("Charlie");
        students.add("Diana");

        // Set attributes to be accessed in JSP
        request.setAttribute("course", "Web Development with Java");
        request.setAttribute("students", students);
        request.setAttribute("total", students.size());

        // Forward data to JSP
        RequestDispatcher rd = request.getRequestDispatcher("students.jsp");
        rd.forward(request, response);
    }
}