import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.*;
import jakarta.servlet.http.*;

// Annotation-based Servlet mapping
@WebServlet("/register")
public class RegistrationServlet extends HttpServlet {

    // Handle GET request
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        out.println("<html><body>");
        out.println("<h2>Welcome to the Registration Page</h2>");
        out.println("<p>Please fill out the form to register.</p>");
        out.println("<a href='registration.html'>Go to Registration Form</a>");
        out.println("</body></html>");
    }

    // Handle POST request (form submission)
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Set response type
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        // Retrieve form data
        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String password = request.getParameter("password");
        String gender = request.getParameter("gender");

        // Display data back to the user
        out.println("<html><body>");
        out.println("<h2>Registration Successful!</h2>");
        out.println("<p><b>Name:</b> " + name + "</p>");
        out.println("<p><b>Email:</b> " + email + "</p>");
        out.println("<p><b>Gender:</b> " + gender + "</p>");
        out.println("<hr>");
        out.println("<a href='registration.html'>Register Another User</a>");
        out.println("</body></html>");
    }
}