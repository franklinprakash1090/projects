<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<html>
<head>
    <title>JSP Demo – Scripting, EL, and JSTL</title>
    <style>
        body { font-family: Arial; background: #f4f4f4; padding: 20px; }
        h2 { color: #007bff; }
        table { border-collapse: collapse; width: 50%; background: #fff; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: center; }
        th { background-color: #007bff; color: white; }
    </style>
</head>
<body>

<%! 
    // JSP Declaration: Declare variables/methods
    int pageVisitCount = 0;
    public int incrementCounter() {
        return ++pageVisitCount;
    }
%>

<%
    // JSP Scriptlet: Execute Java code
    String jspMessage = "Welcome to JSP Scripting and JSTL Demo!";
    int counter = incrementCounter();
%>

<h2><%= jspMessage %></h2>
<p>Page visited: <%= counter %> times (since JSP loaded)</p>

<hr>

<!-- Expression Language (EL) -->
<h3>Course: ${course}</h3>
<h4>Total Students: ${total}</h4>

<!-- JSTL Conditional Rendering -->
<c:if test="${total > 0}">
    <p>✅ List of enrolled students:</p>

    <!-- JSTL Loop Rendering -->
    <table>
        <tr>
            <th>Roll No</th>
            <th>Name</th>
        </tr>

        <c:forEach var="student" items="${students}" varStatus="status">
            <tr>
                <td>${status.index + 1}</td>
                <td>${student}</td>
            </tr>
        </c:forEach>
    </table>
</c:if>

<c:if test="${total == 0}">
    <p>❌ No students enrolled yet.</p>
</c:if>

</body>
</html>