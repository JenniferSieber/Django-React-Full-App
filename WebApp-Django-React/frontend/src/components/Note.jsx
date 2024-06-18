import React from "react";
import "../styles/Note.css";

function Note({ note, onDelete }) {
  const formattedDate = new Date(note.created_at).toLocaleDateString("en-US");

  return (
    <div className="note-container">
      <p className="note-date">{formattedDate}</p>
      <p className="note-title">
        Title: <span>{note.title}</span>
      </p>
      <p className="note-content">{note.content}</p>

      <div>
        {/* <button className="priority-button"onClick={() => priority(note.id)}>Priority</button> */}
        <button className="delete-button" onClick={() => onDelete(note.id)}>
          Delete
        </button>
      </div>
    </div>
  );
}

export default Note;
