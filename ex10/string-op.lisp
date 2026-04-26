;; 1. Get String Size
(defun get-size (text)
  (let ((total 0))
    (loop for char across text do (incf total))
    total))

;; 2. Flip String Order
(defun flip-string (text)
  (let ((result (make-string (get-size text))))
    (let ((size (get-size text)))
      (dotimes (idx size)
        (setf (char result (- size 1 idx)) (char text idx))))
    result))

;; 3. Check if Strings Match
(defun match-strings (a b)
  (let ((size-a (get-size a))
        (size-b (get-size b)))
    (if (/= size-a size-b)
        nil ; Different sizes means no match
        (let ((is-identical t))
          (dotimes (idx size-a)
            (unless (char= (char a idx) (char b idx))
              (setf is-identical nil)))
          is-identical))))

(defun run-string-ops ()
  ;; Processing a single string
  (format t "Enter input string to find the length and it's reverse: ")
  (finish-output)
  (let ((input-text (read-line)))
   
    ;; Processing two strings for matching
    (format t "Enter String 1 for matching: ")
    (finish-output)
    (let ((phrase1 (read-line)))
      (format t "Enter String 2 for matching: ")
      (finish-output)
      (let ((phrase2 (read-line)))

        ;; Display results
        (format t "~%--- Analysis Results ---~%")
        (format t "Length of the string: ~A~%" (get-size input-text))
        (format t "Reversed String: ~A~%" (flip-string input-text))

        (format t "~%--- Comparison Results ---~%")
        (if (match-strings phrase1 phrase2)
            (format t "The comparison of String is EQUAL~%")
            (format t "The comparison of String is Not EQUAL~%"))))))

(run-string-ops)
