def compute_monitoring_metrics(system_type: str, y_true: list, y_pred: list) -> dict:
    """
    Returns a dictionary of metrics.
    """
    # Write code here
    if system_type=="classification":
        tp,tn,fp,fn = 0,0,0,0
        if len(y_pred)!=len(y_true): return None
        for i in range(len(y_true)):
            if (y_pred[i] == y_true[i]) and y_pred[i]==0:
                tn+=1
            elif (y_pred[i] == y_true[i]) and y_pred[i]==1:
                tp+=1
            elif y_pred[i]>y_true[i]:
                fp+=1
            else:
                fn+=1
        recall = tp /(tp+fn) if (tp+fn)!=0 else 0
        precision = tp / (tp+fp) if (tp+fp)!=0 else 0
        accuracy = (tp + tn)/ len(y_pred) if len(y_pred)!=0 else 0
        f1 = 2 * (precision)*(recall)/ (precision+recall) if (precision+recall)!=0 else 0
        metrics_to_return = {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}
    elif system_type == "regression":
        ae,se = 0,0
        for i in range(len(y_true)):
            ae += abs(y_true[i]-y_pred[i])
            se += ((y_true[i]-y_pred[i]) * (y_true[i]-y_pred[i]))
        mae = ae / len(y_true)
        rmse = pow((se / len(y_true)), 0.5)
        metrics_to_return = {"mae": mae, "rmse": rmse}
    elif system_type == "ranking":
        sorted_pair = sorted(zip(y_pred,y_true),key = lambda x: x[0], reverse=True)
        top_3_true = [pair[1] for pair in sorted_pair[:3]]
        relevant = sum(top_3_true)
        total = sum(y_true)
        precision_at_3 = relevant/3.0
        recall_at_3 = relevant/total if total>0 else 0.0
        metrics_to_return = {"recall_at_3": recall_at_3, "precision_at_3": precision_at_3}
    
    return metrics_to_return
    pass