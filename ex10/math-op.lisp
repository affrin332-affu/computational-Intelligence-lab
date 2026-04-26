;; Simple Modulo
(defun my-remainder (a b)
  (if (< a b)
      a
      (my-remainder (- a b) b)))

;; Simple GCD
(defun find-gcd (a b)
  (if (= b 0)
      a
      (find-gcd b (my-remainder a b))))

;; Simple LCM
(defun find-lcm (a b)
  (if (or (= a 0) (= b 0))
      0
      (/ (* a b) (find-gcd a b))))

;; Rectangle Area
(defun area-calc (l w)
  (* l w))

;; Rectangle Perimeter
(defun perimeter-calc (l w)
  (* 2 (+ l w)))

(defun main-math ()
  ;; Part 1: Rectangle info
  (format t "--- Rectangle Work ---~%")
  (format t "Give me the length and width: ")
  (finish-output)
  (let ((l (read))
        (w (read)))
    (format t "Area: ~A~%" (area-calc l w))
    (format t "Perimeter: ~A~%~%" (perimeter-calc l w)))

  ;; Part 2: GCD and LCM info
  (format t "--- Number Work ---~%")
  (format t "Give me two numbers: ")
  (finish-output)
  (let ((n1 (read))
        (n2 (read)))
    (format t "GCD result: ~A~%" (find-gcd n1 n2))
    (format t "LCM result: ~A~%" (find-lcm n1 n2))))

(main-math)
