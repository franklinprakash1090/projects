import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.*;
import jakarta.servlet.http.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.UUID;

@MultipartConfig(fileSizeThreshold = 1024 * 1024 * 2,  // 2MB
                 maxFileSize = 1024 * 1024 * 10,       // 10MB
                 maxRequestSize = 1024 * 1024 * 50)    // 50MB
@WebServlet("/upload")
public class UploadServlet extends HttpServlet {
    private static final String UPLOAD_DIR = "uploads";
    
    // Allowed file types for security
    private static final String[] ALLOWED_EXTENSIONS = {"txt", "pdf", "jpg", "png", "doc", "docx"};

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        try {
            // Get upload path
            String uploadPath = getServletContext().getRealPath("") + File.separator + UPLOAD_DIR;
            
            // Create directory if it doesn't exist
            Path uploadDir = Paths.get(uploadPath);
            if (!Files.exists(uploadDir)) {
                Files.createDirectories(uploadDir);
            }

            // Validate file part exists
            Part filePart = request.getPart("file");
            if (filePart == null || filePart.getSize() == 0) {
                sendError(response, "No file selected for upload");
                return;
            }

            String fileName = filePart.getSubmittedFileName();
            
            // Security validations
            if (!isSafeFileName(fileName)) {
                sendError(response, "Invalid file name");
                return;
            }
            
            if (!isAllowedFileType(fileName)) {
                sendError(response, "File type not allowed");
                return;
            }

            // Generate unique filename to prevent overwrites
            String uniqueFileName = generateUniqueFileName(fileName);
            Path filePath = uploadDir.resolve(uniqueFileName);

            // Save file using try-with-resources
            try (InputStream is = filePart.getInputStream();
                 FileOutputStream fos = new FileOutputStream(filePath.toFile())) {
                
                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = is.read(buffer)) != -1) {
                    fos.write(buffer, 0, bytesRead);
                }
            }

            // Success response
            out.println("<h3>File uploaded successfully!</h3>");
            out.println("<p>Original name: " + fileName + "</p>");
            out.println("<p>Saved as: " + uniqueFileName + "</p>");
            out.println("<a href='upload.html'>Upload Another File</a>");

        } catch (Exception e) {
            sendError(response, "Upload failed: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private boolean isSafeFileName(String fileName) {
        // Basic security check - prevent path traversal attacks
        return fileName != null && 
               !fileName.isEmpty() && 
               !fileName.contains("..") && 
               !fileName.contains("/") && 
               !fileName.contains("\\");
    }

    private boolean isAllowedFileType(String fileName) {
        String extension = getFileExtension(fileName).toLowerCase();
        for (String allowedExt : ALLOWED_EXTENSIONS) {
            if (allowedExt.equalsIgnoreCase(extension)) {
                return true;
            }
        }
        return false;
    }

    private String getFileExtension(String fileName) {
        int lastDot = fileName.lastIndexOf(".");
        return (lastDot == -1) ? "" : fileName.substring(lastDot + 1);
    }

    private String generateUniqueFileName(String originalFileName) {
        String extension = getFileExtension(originalFileName);
        String baseName = originalFileName.substring(0, originalFileName.lastIndexOf('.'));
        String uniqueID = UUID.randomUUID().toString();
        return baseName + "_" + uniqueID + (extension.isEmpty() ? "" : "." + extension);
    }

    private void sendError(HttpServletResponse response, String message) throws IOException {
        response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
        response.getWriter().println("<h3>Error: " + message + "</h3>");
        response.getWriter().println("<a href='upload.html'>Go Back</a>");
    }
}