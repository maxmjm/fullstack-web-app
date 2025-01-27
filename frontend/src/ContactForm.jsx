import { useState } from "react";

const ContactForm = ({}) => {
  // Variable states
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");

  const onSubmit = async (e) => {
    e.preventDefault();

    // Define data
    const data = {
      firstName,
      lastName,
      email,
    };

    // Define url endpoint
    const url = "http://127.0.0.1:5000/create_contact";

    // Set options for request
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };

    // Set request
    const response = await fetch(url, options);

    // Check if request is successful
    if (response.status != 201 && response.status != 200) {
      const data = await response.json();
      alert(data.message);
    } else {
      // Successful
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          id="lastName"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
        <label htmlFor="email">Email:</label>
        <input
          type="text"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <button type="submit">Create Contact</button>
    </form>
  );
};

export default ContactForm;
