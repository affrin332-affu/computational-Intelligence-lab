;; 1. Manual Addition
(defun add-num (a b)
  (if (= b 0)
      a
      (add-num (1+ a) (1- b))))

;; 2. Manual Subtraction
(defun sub-num (a b)
  (if (= b 0)
      a
      (sub-num (1- a) (1- b))))

;; 3. Manual Multiplication
(defun mul-num (a b)
  (cond ((= b 0) 0)
        ((= b 1) a)
        (t (add-num a (mul-num a (1- b))))))

;; 4. Manual Division
(defun div-num (a b)
  (cond ((= b 0) "Error: No division by zero")
        ((< a b) 0)
        (t (1+ (div-num (sub-num a b) b)))))

(defun calculator ()
  ;; Get both numbers first
  (format t "Enter number 1: ")
  (finish-output)
  (let ((num1 (read)))
    (format t "Enter number 2: ")
    (finish-output)
    (let ((num2 (read)))
      ;; Get operator last
      (format t "Enter operator (+ - * /): ")
      (finish-output)
      (let ((op (read)))
        (cond ((eq op '+) (format t "Total: ~A~%" (add-num num1 num2)))
              ((eq op '-) (format t "Total: ~A~%" (sub-num num1 num2)))
              ((eq op '*) (format t "Total: ~A~%" (mul-num num1 num2)))
              ((eq op '/) (format t "Total: ~A~%" (div-num num1 num2)))
              (t (format t "Wrong operator~%")))))))

(calculator)
