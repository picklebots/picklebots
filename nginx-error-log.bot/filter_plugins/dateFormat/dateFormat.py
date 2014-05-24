import datetime

def dateFormat(ip_dt_str,ip_dt_format,op_dt_format):
    
    '''
    date format conversion filter
    '''
    return datetime.datetime.strptime(ip_dt_str, ip_dt_format).strftime(op_dt_format)

class FilterModule (object):

    def filters(self):
        return {"dateFormat": dateFormat}



