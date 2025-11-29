import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.*;
import jakarta.servlet.http.*;

// Annotation for handling multipart form data
@MultipartConfig(fileSizeThreshold = 1024 * 1024 * 2,  // 2MB
                 maxFileSize = 1024 * 1024 * 10,       // 10MB
                 maxRequestSize = 1024 * 1024 * 50)    // 50MB
@WebServlet("/upload")
public class UploadServlet extends HttpServlet {
    private static final String UPLOAD_DIR = "uploads";

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Get upload path inside server
        String uploadPath = getServletContext().getRealPath("") + File.separator + UPLOAD_DIR;

        // Create directory if it doesn’t exist
        File uploadDir = new File(uploadPath);
        if (!uploadDir.exists()) uploadDir.mkdir();

        // Get file part from request
        Part filePart = request.getPart("file");
        String fileName = filePart.getSubmittedFileName();

        // Create file output stream to save uploaded file
        FileOutputStream fos = new FileOutputStream(uploadPath + File.separator + fileName);
        InputStream is = filePart.getInputStream();

        byte[] buffer = new byte[1024];
        int bytesRead;
        while ((bytesRead = is.read(buffer)) != -1) {
            fos.write(buffer, bytesRead);
        }
        fos.close();
        is.close();

        // Send response
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<h3>File uploaded successfully: " + fileName + "</h3>");
        out.println("<a href='upload.html'>Go Back</a>");
    }
}