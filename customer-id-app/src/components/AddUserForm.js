
import React, { useState } from "react";

const AddUserForm = () => {
  const [userId, setUserId] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Check if the userId is provided
    if (!userId) {
      setMessage("User ID is required.");
      setError(true);
      return;
    }

    try {
      // Create the request body in the format expected by the backend
      const requestBody = JSON.stringify({
        body: JSON.stringify({ id: userId }), // Wrap the ID in 'body' as JSON string
      });

      const response = await fetch(
        "https://7firq774sg.execute-api.eu-north-1.amazonaws.com/Prod/customer",
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: requestBody, // Send the request body as expected
        }
      );

      // Log the raw response for debugging
      const data = await response.json();
      console.log("Response data:", data);

      if (!response.ok) {
        // If the response is not ok, display the error message
        setMessage(`Error: ${data.message || 'Something went wrong'}`);
        setError(true);
        return;
      }

      // Check the success message
        if (response.ok) {
            setMessage(`User ${userId} added successfully!`);
            setUserId("")
            setError(false);
        } else {
            // If the response structure is different from what we expect
            setMessage(`Error: ${data.message || 'Unknown error'}`);
            setError(true);
        }
    } catch (err) {
      console.error("Error:", err);
      setMessage("An error occurred. Please try again.");
      setError(true);
    }
  };

  return (
    <div className="form-container">
      <h2>Add a User</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="userId">User ID</label>
        <input
          type="number"
          id="userId"
          name="userId"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
        />
        <button type="submit">Add User</button>
      </form>
      {message && <p className={error ? "error-message" : "success-message"}>{message}</p>}
    </div>
  );
};

export default AddUserForm;