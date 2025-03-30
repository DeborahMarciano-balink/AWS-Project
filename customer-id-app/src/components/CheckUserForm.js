import React, { useState } from "react";

const CheckUserForm = () => {
  const [userId, setUserId] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState(false);

  const handleCheckUser = (e) => {
    e.preventDefault();

    if (!userId) {
      setMessage("You have to have an ID.");
      setError(true);
      return;
    }

    fetch(
      `https://7firq774sg.execute-api.eu-north-1.amazonaws.com/Prod/customer/${userId}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        mode: "cors",
      }
    )
      .then(async (response) => {
        if (response.status === 404) {
          return { notFound: true }; // Cas où l'ID n'existe pas
        }

        if (!response.ok) {
          throw new Error("An error occurred while fetching the user.");
        }

        return response.json();
      })
      .then((data) => {
        if (data.notFound) {
          setMessage("User does not exist.");
        } else {
          setMessage(`User ${data.id} exists.`);
        }
        setError(false);
      })
      .catch((error) => {
        console.error("Error:", error.message);
        setMessage("An error occurred. Please try again.");
        setError(true);
      });
  };

  return (
    <div className="form-container">
            <h2>Check if a User Exists</h2>     {" "}
      <form onSubmit={handleCheckUser}>
                <label htmlFor="userId">User ID</label>
               {" "}
        <input
          type="text"
          id="userId"
          name="userId"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
        />
                <button type="submit">Check User</button>     {" "}
      </form>
           {" "}
      {message && (
        <p className={error ? "error-message" : "success-message"}>{message}</p>
      )}
         {" "}
    </div>
  );
};

export default CheckUserForm;
