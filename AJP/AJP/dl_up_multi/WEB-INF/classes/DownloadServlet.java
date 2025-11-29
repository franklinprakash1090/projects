import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.*;
import jakarta.servlet.http.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@WebServlet("/download")
public class DownloadServlet extends HttpServlet {
    private static final String UPLOAD_DIR = "uploads";
    
    // Allowed file types for download
    private static final String[] ALLOWED_EXTENSIONS = {"txt", "pdf", "jpg", "png", "doc", "docx", "zip"};
    
    // Maximum file size for download (10MB)
    private static final long MAX_FILE_SIZE = 10 * 1024 * 1024;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String fileName = request.getParameter("filename");
        
        // Validate input
        if (fileName == null || fileName.trim().isEmpty()) {
            sendError(response, "Filename parameter is required", HttpServletResponse.SC_BAD_REQUEST);
            return;
        }

        // Security validation
        if (!isSafeFileName(fileName)) {
            sendError(response, "Invalid filename", HttpServletResponse.SC_BAD_REQUEST);
            return;
        }

        // Resolve file path securely
        String uploadPath = getServletContext().getRealPath("") + File.separator + UPLOAD_DIR;
        Path filePath = Paths.get(uploadPath, fileName).normalize();
        
        // Ensure the path stays within the upload directory
        if (!filePath.startsWith(Paths.get(uploadPath).normalize())) {
            sendError(response, "Access denied", HttpServletResponse.SC_FORBIDDEN);
            return;
        }

        File downloadFile = filePath.toFile();

        // Check if file exists and is a regular file
        if (!downloadFile.exists()) {
            sendError(response, "File not found: " + fileName, HttpServletResponse.SC_NOT_FOUND);
            return;
        }

        if (!downloadFile.isFile()) {
            sendError(response, "Invalid file", HttpServletResponse.SC_BAD_REQUEST);
            return;
        }

        // Check file size
        if (downloadFile.length() > MAX_FILE_SIZE) {
            sendError(response, "File too large", HttpServletResponse.SC_REQUEST_ENTITY_TOO_LARGE);
            return;
        }

        // Optional: Check file type
        if (!isAllowedFileType(fileName)) {
            sendError(response, "File type not allowed", HttpServletResponse.SC_FORBIDDEN);
            return;
        }

        try {
            // Set response headers
            String contentType = getServletContext().getMimeType(fileName);
            if (contentType == null) {
                contentType = "application/octet-stream";
            }
            
            response.setContentType(contentType);
            response.setHeader("Content-Disposition", 
                "attachment; filename=\"" + encodeFileName(request, fileName) + "\"");
            response.setHeader("Content-Length", String.valueOf(downloadFile.length()));
            response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate");
            response.setHeader("Pragma", "no-cache");
            response.setHeader("Expires", "0");

            // Stream file to response
            try (InputStream fis = new FileInputStream(downloadFile);
                 OutputStream os = response.getOutputStream()) {
                
                byte[] buffer = new byte[4096]; // Larger buffer for better performance
                int bytesRead;
                while ((bytesRead = fis.read(buffer)) != -1) {
                    os.write(buffer, 0, bytesRead);
                }
                os.flush();
            }

        } catch (IOException e) {
            if (!response.isCommitted()) {
                sendError(response, "Error downloading file: " + e.getMessage(), 
                         HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
            }
            // Log the exception
            getServletContext().log("Error downloading file: " + fileName, e);
        }
    }

    private boolean isSafeFileName(String fileName) {
        // Prevent path traversal attacks and other malicious filenames
        return fileName != null && 
               !fileName.trim().isEmpty() &&
               !fileName.contains("..") &&
               !fileName.contains("/") &&
               !fileName.contains("\\") &&
               !fileName.contains(":") &&
               !fileName.contains("%00") && // Null byte injection
               fileName.matches("[a-zA-Z0-9._\\-()\\[\\] ]+"); // Allow only safe characters
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

    private String encodeFileName(HttpServletRequest request, String fileName) {
        // Handle filename encoding for different browsers
        String userAgent = request.getHeader("User-Agent");
        
        try {
            if (userAgent != null && userAgent.contains("MSIE")) {
                // Internet Explorer
                return java.net.URLEncoder.encode(fileName, "UTF-8");
            } else {
                // Other browsers (RFC 5987)
                return new String(fileName.getBytes("UTF-8"), "ISO-8859-1");
            }
        } catch (UnsupportedEncodingException e) {
            return fileName; // Fallback to original name
        }
    }

    private void sendError(HttpServletResponse response, String message, int statusCode) 
            throws IOException {
        response.setStatus(statusCode);
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h3>Error: " + message + "</h3>");
        out.println("<a href='javascript:history.back()'>Go Back</a>");
        out.println("</body></html>");
    }

    // Optional: Add method to list available files
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        String uploadPath = getServletContext().getRealPath("") + File.separator + UPLOAD_DIR;
        File uploadDir = new File(uploadPath);
        
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        out.println("<html><body>");
        out.println("<h2>Available Files for Download</h2>");
        out.println("<ul>");
        
        File[] files = uploadDir.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isFile() && isAllowedFileType(file.getName()) && isSafeFileName(file.getName())) {
                    out.println("<li><a href='download?filename=" + 
                               java.net.URLEncoder.encode(file.getName(), "UTF-8") + 
                               "'>" + file.getName() + "</a> (" + 
                               formatFileSize(file.length()) + ")</li>");
                }
            }
        }
        
        out.println("</ul>");
        out.println("<a href='upload.html'>Upload New File</a>");
        out.println("</body></html>");
    }

    private String formatFileSize(long size) {
        if (size < 1024) return size + " B";
        else if (size < 1024 * 1024) return (size / 1024) + " KB";
        else return String.format("%.1f MB", size / (1024.0 * 1024.0));
    }
}