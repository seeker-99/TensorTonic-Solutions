Elegant snippets in soln though same thing



        tp = sum(t == 1 and p == 1 for t, p in zip(y_true, y_pred))
        fp = sum(t == 0 and p == 1 for t, p in zip(y_true, y_pred))
        fn = sum(t == 1 and p == 0 for t, p in zip(y_true, y_pred))
        tn = sum(t == 0 and p == 0 for t, p in zip(y_true, y_pred))   



 if system_type == "regression":
        errors = [target - prediction for target, prediction in zip(y_true, y_pred)]
        return {"mae": sum(abs(error) for error in errors) / len(errors), "rmse": (sum(error ** 2 for error in errors) / len(errors)) ** 0.5}
    order = sorted(range(len(y_pred)), key=lambda i: y_pred[i], reverse=True)
    relevant_in_top = sum(y_true[i] == 1 for i in order[:3])
    total_relevant = sum(value == 1 for value in y_true)